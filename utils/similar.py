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
        if(similarity > 0.9 and df['label'][i]=='__label__fake'):
            return('fake news')
        else : return('UNKNOWN')
