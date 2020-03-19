import unittest
import evernote.edam.userstore.constants as UserStoreConstants
from app import EverNote

class TestEvernote(unittest.TestCase):
    # def setUp(self):
    auth_token = "S=s1:U<...>5369"  # 换成自己的 token
    client = EverNote(auth_token)

    tagGuid = "d62cafaa-dcc1-4f41-b727-8a5a1f950f95"
    noteName = "2020-03-13"
    tagName= "时间账"
    notebookName = "时间的朋友"
    
    def test_init(self):
        user_store = self.client.client.get_user_store()
        version_ok = user_store.checkVersion(
            "Evernote EDAMTest (Python)",
            UserStoreConstants.EDAM_VERSION_MAJOR,
            UserStoreConstants.EDAM_VERSION_MINOR
        )
        self.assertIs(version_ok, True, "版本有问题")
    
    def test_getTagGuid(self):
        self.assertEqual(self.client.getTagGuid(self.tagName), self.tagGuid, "获取的 TagGuid 不对")

    def test_getNotebookGuid(self):
        self.assertIsNotNone(self.client.getNotebookGuid(self.notebookName), "获取不到笔记本Guid")

    def test_getNoteGuidByTagGuid(self):
        noteGuid = self.client.getNoteGuidByTagGuid(self.noteName, self.tagGuid)
        self.assertIsNotNone(noteGuid, "无法获取笔记")
    
    def test_getNoteContent(self):
        noteGuid = self.client.getNoteGuidByTagGuid(self.noteName, self.tagGuid)
        content = self.client.getNoteContent(noteGuid)
        self.assertIsNot(content, "", "无法获取到笔记内容")
    
    def test_formatLine(self):
        ftext = self.client.formatLine("测试文本    测试 这是测试    ")
        self.assertEqual(ftext, "<div>测试文本&nbsp; &nbsp; 测试 这是测试&nbsp; &nbsp; </div>", "行格式化失败")
        ftext2 = self.client.formatLine("")
        self.assertEqual(ftext2, "<div><br/></div>", "行无法格式化空行")

    def test_createNote(self):
        content = "测试笔记    测试用\n换行"
        noteGuid = self.client.createNote("测试笔记",content)
        noteContent = self.client.getNoteText(noteGuid)
        self.assertEqual("测试笔记    测试用\n\n换行\n\n", noteContent, "创建笔记失败")
    def test_updateNote(self):
        tagGuid = self.client.getTagGuid("测试")
        noteGuid = self.client.getNoteGuidByTagGuid("测试笔记", tagGuid)
        self.client.updateNote(noteGuid, "添加的内容")
        noteContent = self.client.getNoteText(noteGuid)
        self.assertTrue(noteContent.index("添加的内容")>-1, "更新笔记失败")

if __name__ == '__main__':
    unittest.main(verbosity=0)
    
