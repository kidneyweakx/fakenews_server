#auto update news
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
# SQL
"""
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
"""
global content_list
content_list = []
# crawl (get html data)
def crawl(url):
    headers= {"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
    resp = requests.get(url, headers= headers)
    resp.encoding = 'utf-8'
    return resp.text
# Get HTML datas in contents
def getContent(url, method):
    data = crawl(url)
    #read data in html format
    html = BeautifulSoup(data,"html.parser")
    if method == 1: #台灣事實查核中心
        t = html.find_all("h3", class_= "article-title")
        u = html.select("h3.article-title a")
        nl = html.find("a", string = "下一頁 ›")
        return t ,u, nl
    elif method == 2: #早安健康NEWS
        t = html.find_all("div", id= "essay-title")
        u = html.select("h1 a")
        nl =  html.find("a", string = "下一頁›")
        return t ,u, nl
    elif method == 99:
        #set find area
        t = html.find_all("p")
        #add new content into list
        addC(t)
        print("Content: ", url) 

def createDataFrame(title, u, df, c):
    #put data into a list
    title_list = [p.text.strip() for p in title]
    if c == 1: #台灣事實查核中心
        url_list = ["https://tfc-taiwan.org.tw" + url.get('href') for url in u]
    elif c == 2: #早安健康NEWS
        url_list = [url.get('href') for url in u]
    #check if dataframe exist
    if df.empty:
        df = pd.DataFrame({'title': title_list, 'url': url_list})
    else:
        df = df.append(pd.DataFrame({'title': title_list, 'url': url_list}), ignore_index = True)
    #check fake
    cond1 = df['title'].str.contains('【錯誤】')
    df['tag'] = np.where(cond1, '__label__fake', '__label__undefined')
    df = df[['tag','url','title']]
    return df

#append content to list
def addC(t): 
    temp = []
    for p in t:
        temp.append(p.text.strip())
    content_list.append(temp)

#output file
def output(df, method):
    for url in df['url']:
         getContent(url, 99)
    # CSV
    if  method=='csv':
        path = ""
        df.to_csv(path + 'newsdata.csv', encoding='utf_8_sig', index=False, header=False)
    """ # SQL
    elif method=='sql':
        df['content'] = content_list.astype(str) 
        engine = create_engine('mysql+pymysql://root:@localhost:3306/newsdata')
        df.to_sql('newsdata', engine, if_exists = 'append')
    """

def getSource(): 
    #input news article URL
    #[早安健康NEWS 醫療新聞]undefined https://news.everydayhealth.com.tw/category/news
    #[早安健康NEWS 疾病知識]undefined https://news.everydayhealth.com.tw/category/knowledge
    #fake https://tfc-taiwan.org.tw/articles/category/26/27
    fake_URL = "https://tfc-taiwan.org.tw/taxonomy/term/475"
    undefined_URL = "https://news.everydayhealth.com.tw/category/knowledge"
    
    # create empty DataFrame
    dataframe = pd.DataFrame()
    flag = True
    while(flag):
        t ,u, next_link = getContent(fake_URL, 1)
        #create dataframe
        dataframe = createDataFrame(t,u,dataframe,1) 

        if next_link == None:
            flag = False
        else:
            next_url = "https://tfc-taiwan.org.tw" + next_link["href"]
            fake_URL = next_url
            print("[台灣事實查核中心] Next -> " , next_url)
        time.sleep(3)

    flag = True
    while(flag):        
        t, u, next_link = getContent(undefined_URL, 2)        
        #create dataframe
        dataframe = createDataFrame(t,u,dataframe,2) 
        
        if next_link == None:
            flag = False
        else :
            next_url = next_link["href"]
            undefined_URL = next_url
            print('[早安健康NEWS]Next is:',next_url)
            time.sleep(0.5)
    
    output(dataframe, 'csv')

if __name__ == '__main__':
    getSource()
    del content_list[:]
    print("Successfully")
