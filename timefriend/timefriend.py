import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as Ttypes
from evernote.api.client import EvernoteClient
import html2text
import time
from datetime import datetime, date

class EverNote():
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.client = EvernoteClient(token=auth_token, sandbox=False,china=True)
        self.note_store = self.client.get_note_store()

        self.template = '<?xml version="1.0" encoding="UTF-8"?>'
        self.template +='<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        self.template +='<en-note>%s</en-note>'
    
    def getTagGuid(self, name):
        if name is None:
            return None

        for tag in self.note_store.listTags():
            if tag.name == name:
                return tag.guid

    def getNotebookGuid(self, name):
        notebooks = self.note_store.listNotebooks()
        for notebook in notebooks:
            if notebook.name == name:
                return notebook.guid

    def getNoteGuidByTagGuid(self, title, tagguid):
        f = Ttypes.NoteFilter()
        f.tagGuids = [tagguid]
        notes = self.note_store.findNotes(self.auth_token, f, 0, 999).notes
        for note in notes:
            if note.title == title:
                return note.guid

    def getNoteContent(self, guid):
        note = self.note_store.getNote(self.auth_token, guid, True,False,False,False)
        return note.content

    def getNoteText(self, guid):
        content = self.getNoteContent(guid)
        notetext = html2text.html2text(content)
        return notetext

    def analysisNote(self, notetext):
        lines = notetext.split('\n\n')
        # 分类
        # 开始时间，结束时间 内容，分类，成本
        startTime = lines[0].split(" "*4)[0]  # 当天记录的开始时间
        # return lines[0].split(" "*4)
        rows = []
        statistics = {
            "total": 0,
            "group": {}
        }
        begin = startTime  # 每个记录的开始时间
        for l in lines[1:]:
            if not l.strip():
                continue
            row = {}
            parts = l.split(" "*4)
            row['begin'] = begin
            row['end'] = parts[0]
            row['description'] = parts[1]
            row['type'] = parts[2]
            row['cost'] = parts[3]
            rows.append(row)

            group = statistics["group"].get(row['type'], 0)
            group += int(row['cost'])
            statistics["group"][row['type']] = group
            begin = row['end']
        if startTime > begin:
            statistics['total'] = difftime("2020-01-02 " + begin + ":00", "2020-01-01 " + startTime + ":00", "m")
        else:
            statistics['total'] = difftime("2020-01-01 " + begin + ":00", "2020-01-01 " + startTime + ":00", "m")
        print(startTime," ", begin)
        return  statistics

    def formatNote(self, text): # 将文字转换为印象笔记格式
        content = []
        for line in text.split("\n"):
            content.append(self.formatLine(line))
        return "".join(content)

    def formatLine(self, line):
        tabstr = "&nbsp; &nbsp; "
        if line:
            return "<div>" + line.replace(" "*4, tabstr).replace("\t", tabstr) + "</div>"
        else:
            return "<div><br/></div>"

    def createNote(self, title, content, tag=None, notebook="随手记"):
        # 得到 tags
        tagGuid = self.getTagGuid(tag) if tag else None

        if tagGuid is None and tag is not None:
            tagGuid = self.createTag(tag)

        # 得到 notebook
        notebookGuid = self.getNotebookGuid(notebook)
        # 格式化文本
        noteContent = self.formatNote(content)
        # 构造 note 对象
        note = Types.Note()
        note.title = title
        if tagGuid:
            note.tagGuids = [tagGuid]
        note.notebookGuid = notebookGuid
        note.content = self.template % noteContent

        # 存入
        enote = self.note_store.createNote(self.auth_token, note)

        return enote.guid

    def createTag(self, name):
        tag = Types.Tag()
        tag.name = name
        tag = self.note_store.createTag(self.auth_token, tag)
        return tag.guid

    def updateNote(self, guid, content, operation='a'):
        """
        更新指定笔记的内容
        type： a 追加，r 替换
        """
        note = self.note_store.getNote(self.auth_token, guid, True,False,False,False)
        noteContent = self.formatNote(content)

        if operation == 'a':
            note.content = note.content.replace("</en-note>", "") + noteContent + "</en-note>"
        elif operation == 'r':
            note.content =  self.template % noteContent
        else:
            raise "未知操作符 " + operation

        self.note_store.updateNote(self.auth_token, note)
        return note.guid

def time2datetime(a_time, str_format="%Y-%m-%d %H:%M:%S"):
    if type(a_time) == datetime:
        return a_time
    if type(a_time) == date:
        return a_time
    if type(a_time) == time.struct_time:
        return datetime.utcfromtimestamp(time.mktime(a_time))
    if type(a_time) == float:
        return datetime.utcfromtimestamp(a_time)
    if type(a_time) == str:
        return datetime.strptime(a_time, str_format)
    pass

def difftime(timea, timeb, unit='S'):
    # 进行格式转换
    timea = time2datetime(timea)
    timeb = time2datetime(timeb)

    timediff = timea - timeb
    # 转换为秒
    timecount = timediff.days*24*3600
    timecount += timediff.seconds
    timecount += timediff.microseconds/1000000

    if unit == 'd':  # 日
        return timecount / (24*3600)
    if unit == 'm':  # 分
        return timecount / 60
    if unit == 'h':  # 时
        return timecount / 3600
    if unit == 'S':  # 秒
        return timecount
    if unit == 's':  # 毫秒
        return timecount * 1000
    if unit == 'f':  # 微妙
        return timecount * 1000000
    if unit == 'w':  # 周
        return timecount / (24*3600*7)
    if unit == 'M':  # 月
        return timecount / (24 * 3600 * 30)

if __name__ == '__main__':
    # 集成
    auth_token = "S=s1:U<...>5369" # 换成自己的 token
    client = EverNote(auth_token)  # 创建代理实例

    # 获取日志 text 内容
    tagGuid = client.getTagGuid("时间账")
    noteGuid = client.getNoteGuidByTagGuid("2020-03-18", tagGuid)
    noteText = client.getNoteText(noteGuid)

    ret = client.analysisNote(noteText)  # 解析并分析

    client.updateNote(noteGuid, ret.result) # 添加分析结果
