import os
from PIL import Image
import pytesseract
from utils import simgraphql # Utils資料夾中similar.py

# tesseract 安裝路徑 (Windows/Linux 問題)
# pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '‪‪D:\\Software\\Tesseract-OCR\\tesseract.exe'

def ocr(img):
    # 執行OCR
    text = pytesseract.image_to_string(img, lang='chi_tra')
    print('tesseract text :',text)
    # 運用Similar.py 中的 classifier 函式辨識假新聞
    # truth=similar.classifier(text)
    truth = simgraphql.cofactapi(text)
    return(truth)

