import fitz
import os
from PIL import Image
import csv
import pytesseract
zoom_x = 10.0
zoom_y = 10.0
doc = fitz.open('qr_codes.pdf')
# def convert_to_imgs(zoom_x,zoom_y):
#     # for page in doc:
#     #     mat = fitz.Matrix(zoom_x,zoom_y)
#     #     pix = page.get_pixmap(matrix=mat)
#     #     pix.save('imgs/page-%i.png' % page.number)
def convert_imgs(path):
    all_photos = os.listdir(path)
    for i in range(len(all_photos)):
        img = Image.open(f'{path}{all_photos[i]}')
        width,height = img.size
        new_img = img.crop((100,1100, width-100,height-400))
        new_img.save(f'reform_photos/{all_photos[i]}')
# convert_imgs('imgs/')
dt = []
def check_photo(path):
    all_photos = os.listdir(path)
    for i in range(len(all_photos)):
        pytesseract.pytesseract.tesseract_cmd = r'C:/APPS/tesseract/Tesseract-OCR/tesseract'
        with Image.open(f'reform_photos/{all_photos[i]}') as img:
            # Распознаем текст на изображении
            text = pytesseract.image_to_string(img).split()
            text = ''.join(text)
            dt.append(text)
def append_to_csv():
    for i in range(len(dt)):
        with open('csv_new.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(dt[i])
check_photo('reform_photos/')
append_to_csv()
print(dt)
