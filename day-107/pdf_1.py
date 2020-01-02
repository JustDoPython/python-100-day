# pdf_1.py
 
# 导入库
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
 
# 设置文档密码
password = ''
 
#打开pdf文件
fp = open('pdfminer.pdf','rb')
 
#从文件句柄创建一个pdf解析对象
parser = PDFParser(fp)
 
#创建pdf文档对象，存储文档结构
document = PDFDocument(parser,password)
 
#创建一个pdf资源管理对象，存储共享资源
rsrcmgr = PDFResourceManager()
 
#创建一个device对象
device = PDFDevice(rsrcmgr)
 
#创建一个解释对象
interpreter = PDFPageInterpreter(rsrcmgr, device)
 
#处理包含在文档中的每一页
for page in PDFPage.create_pages(document):
	interpreter.process_page(page)