import os
from PIL import Image
import pytesseract
# tesseract 安裝路徑
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr(path):
    img = Image.open(path)
    # 執行OCR
    text = pytesseract.image_to_string(img, lang='chi_tra')
    return(text)

# TODO : 連結比對系統 

