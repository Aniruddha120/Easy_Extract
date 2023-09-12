'''
Easy_Extract: An easy program to extract text from PDF and JPG file

Developped By: Aniruddha Sarkar 
Please Make Sure you have Pre Installed Tesseract, pdf2image and OpenCV. Also add the installtion path of Tesseract to System Environment Variables. Input the file path without Quotations. 

'''
#importing Libraries
import pytesseract
import cv2
from pdf2image import convert_from_path
import glob

# inputting file path
path = input('Please Make Sure you have Pre Installed Tesseract, pdf2image and OpenCV at the same time add the installtion path of Tesseract to System Environment Variables. Input the file path without Quotations : ')

if path.endswith('.pdf'):
        pdfs = glob.glob(path)

        for pdf_path in pdfs:
            pages = convert_from_path(pdf_path, 500)

        for pageNum,imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob,lang='eng')

            with open(f'{pdf_path}.txt', 'a') as the_file:
                the_file.write(text)
                print(text)
elif path.endswith('.jpg'or'.png'):
        image = cv2.imread(path)
        retval, image = cv2.threshold(image,200,255, cv2.THRESH_BINARY)
        image = cv2.resize(image,(0,0),fx=3,fy=3)
        image = cv2.GaussianBlur(image,(11,11),0)
        image = cv2.medianBlur(image,9)
        text = pytesseract.image_to_string(image)
        print(text)
else: 
        print('File not Supported')