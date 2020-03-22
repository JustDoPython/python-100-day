import zxing
from MyQR import myqr

reader = zxing.BarCodeReader()
barcode = reader.decode('gzh.jpg')
# print(str(barcode.parsed))
myqr.run(words=str(barcode.parsed),
         version=1,
         picture='my.gif',
         colorized=True,
	     save_name='gmyqr.gif')