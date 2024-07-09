#import random       #導入一個亂數
#random.randint()   產生指定數值範圍與數量的隨機整數
"""終極密碼遊戲

import random       #導入一個亂數
min_num = 1         #設定密碼範圍的最大最小值
max_num = 100
ans_num=random.randint(1,100)       #random.randint()   產生指定數值範圍與數量的隨機整數
gus_num=0           #猜的數值初始設定為0
while gus_num != ans_num :
    gus_num = input(f"請輸入{min_num}~{max_num}:")
    gus_num=int(gus_num)
    if gus_num < min_num or gus_num > max_num :
        print("數值範文錯誤")
        continue
    elif gus_num != ans_num and gus_num < ans_num :
        min_num = gus_num
    elif gus_num != ans_num and gus_num > ans_num :
        max_num = gus_num
else :
    print(ans_num,"答對了!")        

"""

"""#讓用戶輸入一個數值,求其因數
num=int(input("請輸入一個值:"))
fac=""
for x in range(1,num+1) :
    y = num // x
    if y < x :
        break
    if num % x == 0 :
        fac = fac + f"{x}, "
        if x != y :
            fac = fac + f"{y},"
print(fac)
#用資料集輸出
num=int(input("請輸入一個值:"))
lst=[]
for x in range(1,num+1) :
    y = num // x
    if y < x :
        break
    if num % x == 0 :
        lst.append(x)
        if x != y :
            lst.append(y)

print(lst,len(lst))

"""    

"""#隨機產出10個介於1~100的整數清單,將內容的奇數與偶數分別列印出來
ls = []
for x in range (10) : 
    ls.append(random.randint(1,100))
#奇數
for n in ls :
    if n % 2 == 1 :
        print(n)
#偶數
for n in ls :
    if n % 2 == 0 :
        print(n) 
"""
"""
import random
ls=[random.randint(1,100) for x in range(10) ]
print(ls)
print([n for n in ls if n % 2 == 1])
print([n for n in ls if n % 2 == 0])
"""
"""#隨機產出20個介於1~100的整數Tuple,將每一個內容數值不可重複輸出值及次數
import random
tp=tuple([random.randint(1,10)for n in range(20)])
print(tp)
for x in range(len(tp)) :
    num=tp[x]
    if x == tp.index(num) :
        print(num, "=>數量" ,tp.count(num))
"""