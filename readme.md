# Fakenews OCR Detect 
*使用前請先閱讀該文件!!!!!*

### 📎 基本說明
可使用圖片轉文字來偵測假新聞的伺服器實作。

[範例網站](https://kidneyweakx.nctu.me/)

### 🛠 開發環境
- **IDE**: Visual Studio 2019 or VScode
- **Python**: Python 3.7.6 :: Anaconda, Inc on Win32
- **如果你是Linux環境**: 執行該檔案完成環境建置 [aptrequired.sh](./aptrequired.sh)
```[shell]
# 在終端機中執行該行指令
bash aptrequired.sh
```

### 📜 功能列表
- Flask Server
    - [x] [主畫面](./templates/index.html)
    - [x] [上傳圖片](./templates/upload.html)
    - [x] 圖形介面
    - [x] CSS美化
    - [x] 返回假新聞回饋功能 
- Tesseract
    - [x] [圖片轉文字(OCR)功能](./utils/tesseract.py)
- Texts Compare
    - [x] [<del>Flairs Model</del>](./archives/ispam.py)
    - [ ]  SpaCy 相似度比對
        - [x] [假新聞比對](./utils/similar.py)
        - [ ] 真新聞比對
        - [ ] 比對加速
        - [ ] 與資料庫中資料做對比
        - [ ] 詞性情感比對
    - [x] (備案) 假新聞辨識模型 (無中文版)
- Crawl
    - [x] 爬取新聞資料
    - [x] 自動爬取新增資料
    - [x] 將爬取資料匯入資料庫
- Deploy
    - [x] [UWSGI 部屬](./uwsgi.ini)
    - [x] [Nginx 反向代理](./nginxsetting.txt)
    - [x] AWS EC2 上線
    - [x] HTTPS 安全性
    - [ ] 穩定度測試 



### 🔔 環境執行前注意
- 需先下載 tesseract軟體 [Windows載點](https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html)
- [`tesseract.py`](./utils/tesseract.py) 根據你的tesseract應用程式下載位置更改 Line 7 值 
``` [python]
# 先執行該行程式將所有依賴套件下載好
pip install -r requirement.txt
```
[Requirement.txt](./requirement.txt)
NOTE:*UWSGI可視情況不下載*
- [`spacy`](https://spacy.io/usage) download chinese(zh_core_web_sm)
``` [python]
# 語言包需額外下載
python -m spacy download zh_core_web_sm
```


### 💻 執行
將爬取的CSV檔放入[data](./utils/data)資料夾便可執行
```[python]
# 執行該段後即可透過 localhost:port來瀏覽
python app.py
```

### 🔧 依賴套件
*主要運用這些套件*
- [伺服器Flask](https://flask.palletsprojects.com/)
- [NLP套件SpaCy](https://spacy.io/)
- [OCR套件Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
- [資料處理Pandas](https://pandas.pydata.org/)


