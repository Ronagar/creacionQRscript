from pathlib import Path
import qrcode
from PIL import Image
import csv 

with open('alumnos.csv') as file:
    reader = csv.DictReader(file)
    headers = [header.strip() for header in reader.fieldnames]
    for row in reader:
        student=row.get(headers[1])+row.get(headers[0])
        

        #Creation of the path if neccessary
        Path('./outputs/'+student).mkdir(parents=True, exist_ok=True)
        

        for letter in ('a','b','c'):
            print(letter)
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            #extract the student id from the dataSet
            data = row.get(headers[2])
            #Feed the QR Code data
            data = data+'_'+letter
            print(data)
            QRcode.add_data(data)
            QRcode.make

            #Creation of the image
            QRimg = QRcode.make_image()
        
            #Save the image .png
            path = './outputs/'+student+'/'+data+'.png'
            QRimg.save(path)
     
file.close()




