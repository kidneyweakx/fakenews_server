
# 作業系統
import os
import sys

# 字碼轉換
import codecs

# 數值運算
import numpy as np
import numpy.linalg as la

# 自然語言處理
import nltk
#from nltk.corpus import stopwords

# 移除標點符號
def removeChineseStopWords(textFile):
    newTextFile = textFile

    chineseFilter = ['，', '。', '、', '；', '：', '？', '「', '」']

    for chin in chineseFilter:
        newTextFile = newTextFile.replace(chin, ' ')
    
    return newTextFile
    
# 讀取中文檔案
def getTokensFromFile(textFileName):
    textFileHandle = codecs.open(textFileName, 'rU','utf8')

    textContent = textFileHandle.read()
    
    #for word in stopwords.words('english'):
        #textContent = textContent.replace(word, ' ')
       
    textTokens = nltk.word_tokenize(removeChineseStopWords(textContent))
    
    textFileHandle.close()

    return textTokens

def getTokensFromStr(textContent):    
    
    #for word in stopwords.words('english'):
        #textContent = textContent.replace(word, ' ')
       
    textTokens = nltk.word_tokenize(removeChineseStopWords(textContent))

    return textTokens

# 字詞頻度表
def getTokenFreqList(textTokens):
    tokenFrequency = nltk.FreqDist(textTokens)

    # 刪除單一字
    for word in list(tokenFrequency):
        if len(word) == 1:
            tokenFrequency.pop(word)
    
    # 刪除數字
    for word in list(tokenFrequency):
        try:
            val = float(word)
            tokenFrequency.pop(word)
        except:
            pass
    
    # 刪除廢詞
    chineseFilter = ['可能', '不過', '如果', '恐怕', '其實', '進入', '雖然', '這麼',
                     '處於', '因為', '一定']

    for word in tokenFrequency:
        if word in chineseFilter:
            tokenFrequency.pop(word)
    
    return tokenFrequency

# 計算兩向量的距離：問題所在
def getVecDistance(vec1, vec2):
    if la.norm(vec1) == 0 or la.norm(vec2) == 0:
        return -1
    
    return round(np.inner(vec1, vec2) / (la.norm(vec1) * la.norm(vec2)), 4)
    
# 計算文件相似度    
def getDocSimilarity(wordFrequencyPair, minTimes=1):
    dict1 = {}
    for key in wordFrequencyPair[0].keys():
        if wordFrequencyPair[0].get(key, 0) >= minTimes:
            dict1[key] = wordFrequencyPair[0].get(key, 0)

    dict2 = {}
    for key in wordFrequencyPair[1].keys():
        if wordFrequencyPair[1].get(key, 0) >= minTimes:
            dict2[key] = wordFrequencyPair[1].get(key, 0)

    for key in dict2.keys():
        if dict1.get(key, 0) == 0:
            dict1[key] = 0
        
    for key in dict1.keys():
        if dict2.get(key, 0) == 0:
            dict2[key] = 0
        
    v1 = []
    for w in sorted(dict1.keys()):
        v1.append(dict1.get(w))
    
    v2 = []    
    for w in sorted(dict2.keys()):
        v2.append(dict2.get(w))

    result = 0
    try:
        result = getVecDistance(v1, v2) # 計算兩向量的距離
    except(RuntimeError, TypeError, NameError):
        pass
        
    return result

# 主程式
def compare(txt):   
    filelist = []
    path= os.path.join(os.path.dirname(__file__),"data")
    filelist.append(os.path.join(path,"train.txt")) # 設定訓練集路徑
    filelist.append(os.path.join(path,"test.txt")) # 設定測試集路徑

    trainFile = filelist[0]
    trainTokens = getTokensFromFile(trainFile)
    trainTokenFrequency = getTokenFreqList(trainTokens)
    
    testTokens = getTokensFromStr(txt)
    testTokenFrequency = getTokenFreqList(testTokens)
    
    wordFrequencyPair = [trainTokenFrequency, testTokenFrequency]
    return ("相似度："+ str(getDocSimilarity(wordFrequencyPair, 1)))

if __name__ == '__main__':
    print(compare(''))
    