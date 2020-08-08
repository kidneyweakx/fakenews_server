import os
from dotenv import load_dotenv, find_dotenv
import jieba.analyse
import pymysql

def ana(txt):
    load_dotenv(find_dotenv())
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASS")
    conn = pymysql.connect(host=db_host, port=int(db_port), user=db_user, passwd=db_pass, db='newsdata', charset='utf8')
    kw = jieba.analyse.textrank(txt, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM newsdata WHERE content LIKE '%s'"%('%'+kw[0][0]+'%'))
    data = cursor.fetchall()
    label = data[0][1]
    if label == '__label__fake': return('FakeNews')
    elif label == '__label__undefined': return('Undefined')
    elif label == '__label__true': return('truenews')
    return('UNKNOWN')




if __name__ == "__main__":
    print(ana('楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了'))