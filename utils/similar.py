import os
import spacy
import pandas as pd
import numpy as np

def classifier(text) :
    path = os.path.join('./utils/data/','data600.csv')
    df = pd.read_csv(path, names=['label', 'source', 'paragraph', 'truth'])
    nlp = spacy.load('zh_core_web_sm')
    ocrp = nlp(text)
    dsize = (df.size) / 4
    for i in range(dsize.astype('int16')) : 
        dfp = nlp(df['paragraph'][i])
        similarity = ocrp.similarity(dfp)
        #print(similarity)
        if(similarity > 0.9):
            label = df['label'][i]
            if label == '__label__fake': return('FakeNews')
            elif label == '__label__undefined': return('Undefined')
            break

    return('UNKNOWN')

if __name__ == "__main__":
    print(classifier('楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了'))