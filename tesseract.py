import os
from PIL import Image
import pytesseract
import ispam

# tesseract 安裝路徑 (windows 問題)
# pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr(path):
    img = Image.open(path)
    # 執行OCR
    text = pytesseract.image_to_string(img, lang='eng')#lang='chi_tra')
    print(text)
    # 辨識垃圾訊息
    spam=ispam.spamcleaner(text)
    return(spam)

