import os
import spacy
import pandas as pd
import requests
import json

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

def cofactapi(news):
    news = '"' + news + '"'
    query = """query {
    ListArticles(
        filter: { moreLikeThis: { like: %s } }
            orderBy: [{ _score: DESC }]
        first: 3
        ) {
        edges {
            node {
            # id
            text
            #hyperlinks {
            #    url
            #}
        articleReplies {
            reply {
                #id
                text
                type
                reference
            }
            }
            }
        }
    }
    }"""%(news)
    url = "https://cofacts-api.g0v.tw/graphql"
    r = requests.post(url, json={'query': query})
    r.encoding = 'utf-8'
    data = json.loads(r.text)
    label = data['data']["ListArticles"]['edges'][0]['node']['articleReplies'][0]['reply']['type']
    if label == 'RUMOR': return('FakeNews')
    elif label == 'NOT_RUMOR': return('Truth')

if __name__ == "__main__":
    # 單檔測試文本
    print(classifier('楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了'))
    print(cofactapi("楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了"))