import os
import spacy
import pandas as pd

def classifier(text) :
    # 將爬蟲資料csv路徑加入
    path = os.path.join('./utils/data/','data600.csv')
    df = pd.read_csv(path, names=['label', 'source', 'paragraph', 'truth'])
    # 運用SpaCy 中文NLP處理模型
    nlp = spacy.load('zh_core_web_sm')
    ocrp = nlp(text)
    # 將dataframe label總數計算並除label數
    dsize = (df.size) / 4
    # 將所有內文都轉換成SpaCy格式來辨識相似度
    for i in range(dsize.astype('int16')) : 
        dfp = nlp(df['paragraph'][i])
        similarity = ocrp.similarity(dfp)
        #print(similarity)
        # 該處可能還需稍微調整
        if(similarity > 0.95):
            print(similarity)
            label = df['label'][i]
            if label == '__label__fake': return('FakeNews')
            elif label == '__label__undefined': return('Undefined')
            elif label == '__label__true': return('truenews')
            break

    return('UNKNOWN')

if __name__ == "__main__":
    # 單檔測試文本
    print(classifier('楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了'))