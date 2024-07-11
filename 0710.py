"""#利用random函式產生5個介於1~10之間不重複的值
import random       #導入亂數
s = set()
n = 0       #這邊為while迴圈跑的次數
while len(s) < 5 :
    n += 1          #迴圈次數
    s.add(random.randint(1,10))     #s.加入#random.randint()   產生指定數值範圍與數量的隨機整數
print(s,n)
"""

"""
讓用戶分別輸入姓名、國文成績、數學成績、英文成績
當用戶於任何時候輸入空白時結束輸入
將資料輸出如下
姓  名 國文 數學 英文 平均
-------- ---- ---- ---- -----
12345678 1234 1234 1234 123.4
12345678 1234 1234 1234 123.4
12345678 1234 1234 1234 123.4
"""
"""
date=[]     #建構空白清單
while True :                                    #構成無窮迴圈。也可wh
    stud = {"name" : "",
            "chin" : 0 ,
            "engl" : 0 ,
            "math" : 0 }
    stud["name"] = input("姓名:")
    if stud["name"].strip() == "" :             #.strip() 去除空白      #如果stud["name"]去除空白等於沒東西,就break(結束)
        break
    #國文
    stud["chin"] = input("國文:")
    if stud["chin"].strip() == "" :
        break
    else:
        stud["chin"] = int(stud["chin"])        #轉整數,後面才有辦法計算
    #數學
    stud["math"] = input("數學:")
    if stud["math"].strip() == "" :
        break
    else:
        stud["math"] = int(stud["math"])
    #英文
    stud["engl"] = input("英文:")
    if stud["engl"].strip() == "" :
        break
    else:
        stud["engl"] = int(stud["engl"])
    #---
    date.append(stud)           #將stud加進date 中
#---
print("姓  名 國文 數學 英文 平均")
print("-------- ---- ---- ---- -----")
for d in date :
    avg=(d["chin"]+d["engl"]+d["math"])/3
    print("{:8s}{:4d}{:4d}{:4d}{:5.1f}".format(d["name"],d["chin"],d["engl"],d["math"],avg))
"""
#資料庫讀取範圍
import sqlite3
#建立資料庫連線
conn=sqlite3.connect("data.db")
curs=conn.cursor()
#抓取資料庫資料
curs.execute("SELECT * FROM MOCK_DATA WHERE id <=5")
#打包欄位名稱
columns=[col[0] for col in curs.description]
#for col in curs.description        #可與下列縮寫成上列
#    columns.append(col[0])
print(curs.fetchall())      #把全部讀取到的內容都列印出來