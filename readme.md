# fakenews OCR detect
*Read this menu first!!!!!*

### Enviroment
Visual Studio 2019 or VScode

### Notice
[Requirement](./requirement.txt)
- flair library not the necessity
- [spacy](https://spacy.io/usage) download chinese(zh_core_web_sm)
- [tesseract.py](./utils/tesseract.py) Line 7 accroding to your tesseract application location to change the value

### Run
``` [python]
pip install -r requirement.txt
python -m spacy download zh_core_web_sm
```
put data in [data](./utils/data) folder
`python app.py`
