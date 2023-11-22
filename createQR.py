import qrcode
from PIL import Image

owner='miguel'
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

#Feed the QR Code data
datos='Hola buenas tardes :D'
QRcode.add_data(datos)
QRcode.make

#Creation of the image
QRimg = QRcode.make_image()
path = './'+owner+'.png'
QRimg.save(path)

