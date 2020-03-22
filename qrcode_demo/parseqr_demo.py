import zxing
from MyQR import myqr

reader = zxing.BarCodeReader()
barcode = reader.decode('myqr.gif')
print(barcode.parsed)