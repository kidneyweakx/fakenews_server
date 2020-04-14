import os
from PIL import Image
import pytesseract
# import similar
import ispam
# tesseract 安裝路徑
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr(path):
    img = Image.open(path)
    # 執行OCR
    text = pytesseract.image_to_string(img, lang='eng')#lang='chi_tra')
    print(text)
    # sim = similar.compare(text)
    sim=ispam.spamcleaner(text)
    return(sim)

# TODO : 連結比對系統 

