import time
import jieba.posseg as pseg

def ana(txt):
    start = time.time()
    words = pseg.cut(txt)
    for w in words: print(w.word, w.flag)
    return('---%f time---' %(time.time()-start))
     




if __name__ == "__main__":
    print(ana('楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了'))