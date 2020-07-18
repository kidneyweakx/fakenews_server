#auto update news
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import time

def createDataFrame(title, u, df, c):
    #put data into a list
    title_list = [p.text.strip() for p in title]
    if c == 1:#台灣事實查核中心
        url_list = ["https://tfc-taiwan.org.tw" + url.get('href') for url in u]
    elif c == 2:#早安健康NEWS
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

def getSource(): 
    #input news article URL
    #[早安健康NEWS 醫療新聞]undefined https://news.everydayhealth.com.tw/category/news
    #[早安健康NEWS 疾病知識]undefined https://news.everydayhealth.com.tw/category/knowledge
    #fake https://tfc-taiwan.org.tw/articles/category/26/27

    fake_URL = "https://tfc-taiwan.org.tw/taxonomy/term/475"
    undefined_URL = "https://news.everydayhealth.com.tw/category/knowledge"

    dataframe = pd.DataFrame()
    
    for _ in range(11):
        req = request.Request(fake_URL)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
        response = request.urlopen(req)
        data = response.read().decode("utf-8")
        
        #read data in html format
        html = BeautifulSoup(data,"html.parser")
        
        #set find area
        t = html.find_all("h3", class_= "article-title")
        u = html.select("h3.article-title a")

        #create dataframe
        dataframe = createDataFrame(t,u,dataframe,1) 
        
        next_link = html.find("a", string = "下一頁 ›")
        next_url = "https://tfc-taiwan.org.tw/taxonomy/term/475" + next_link["href"]
        fake_URL = next_url

        time.sleep(3)
    
    for _ in range(50):
        req = request.Request(undefined_URL)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
        response = request.urlopen(req)
        data = response.read().decode("utf-8")
        
        #read data in html format
        html = BeautifulSoup(data,"html.parser")
        
        #set find area
        t = html.find_all("div", id= "essay-title")
        u = html.select("h1 a")

        #create dataframe
        dataframe = createDataFrame(t,u,dataframe,2) 
        
        next_link = html.find("a", string = "下一頁›")
        next_url = "https://news.everydayhealth.com.tw/category/knowledge" + next_link["href"]
        undefined_URL = next_url
        
        time.sleep(3)

    outputCsv(dataframe)

global content_list
content_list = []

#append content to list
def addC(t): 
    temp = []
    for p in t:
        temp.append(p.text.strip())
    content_list.append(temp)

def getContent(url):
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
    response = request.urlopen(req)
    data = response.read().decode("utf-8")

    #read data in html format
    html = BeautifulSoup(data,"html.parser")

    #set find area
    t = html.find_all("p")
    
    #add new content into list
    addC(t)
          
    time.sleep(3) 

#output csv file
def outputCsv(df):
    for url in df['url']:
         getContent(url)
    df['content'] = content_list  
    path = ""
    df.to_csv(path + 'newsdata.csv', encoding='utf_8_sig', index=False, header=False)

def sleeptime(h,m,s):
    return h*3600 + m*60 + s

#update every 6 hours
second = sleeptime(0,1,0)

if __name__ == '__main__':
    while True:  
        getSource()
        del content_list[:]
        time.sleep(second)
