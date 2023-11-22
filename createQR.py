from pathlib import Path
import qrcode
from PIL import Image
import csv 

with open('alumnos.csv') as file:
    reader = csv.DictReader(file)
    headers = [header.strip() for header in reader.fieldnames]
    for row in reader:
        #print(row.get(headers[0]),row.get(headers[2]))
        #print(row['nombre'], row['ID'])
        student=row.get(headers[1])+row.get(headers[0])
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

        #Feed the QR Code data
        data = row.get(headers[2])
        QRcode.add_data(data)
        QRcode.make

        #Creation of the path if neccessary
        Path('./outputs/'+student).mkdir(parents=True, exist_ok=True)
        #Creation of the image
        QRimg = QRcode.make_image()
        
        #Save the image .png
        path = './outputs/'+student+'/'+data+'.png'
        QRimg.save(path)
     
file.close()




