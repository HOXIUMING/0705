
"""#讓用戶輸入姓名當日氣溫，18度以下顯示”寒冷”，18~30度顯示”舒適”，30度以上顯示”炎熱”
name=input("請問您的大名是:")
#temperatture氣溫
temperatture=float(input("現在溫度是:"))

#第三格式化
if temperatture < 18 :
    print("您好%s,現在溫度是%d度,是寒冷的,注意保暖!"%(name,int(temperatture)))
elif temperatture < 30 :
    print("您好%s,現在溫度是%d度,是舒適的,祝您今日愉快!"%(name,int(temperatture)))
else:print("您好%s,現在溫度是%d度,是炎熱的,請多補充水分!"%(name,int(temperatture)))

#第二格式化
if temperatture < 18 :
    print("您好{:s},現在溫度是{:d}度,是寒冷的,注意保暖!".format(name,int(temperatture)))
elif temperatture < 30 :
    print("您好{:s},現在溫度是{:d}度,是舒適的,祝您今日愉快!".format(name,int(temperatture)))
else:print("您好{:s},現在溫度是{:d}度,是炎熱的,請多補充水分!".format(name,int(temperatture)))

#第一格式化
if temperatture < 18 :
    print(f"您好{name:s},現在溫度是{int(temperatture):d}度,是寒冷的,注意保暖!")
elif temperatture < 30 :
    print(f"您好{name:s},現在溫度是{int(temperatture):d}度,是舒適的,祝您今日愉快!")
else:print(f"您好{name:s},現在溫度是{int(temperatture):d}度,是炎熱的,請多補充水分!")

#一般直接代入
temperatture=int(temperatture)          #將溫度轉為整數
if temperatture < 18 :
    print("您好",name,",現在溫度是",temperatture,"度,是寒冷的,注意保暖!")
elif temperatture < 30 :
    print("您好",name,",現在溫度是",temperatture,"度,是舒適的,祝您今日愉快!")
else:print("您好",name,",現在溫度是",temperatture,"度,是炎熱的,請多補充水分!")
"""

"""#讓用戶依序輸入姓名、性別、婚姻狀態，並依顯示其尊稱Miss(小姐)，Mrs(太太)，Ms(女士)，Mr(先生) 及其姓名。

#例：Angle Novak, Female, Not married => Miss Novak
#Cindy Connor, Male, Married => Mr. Connor
#Emma Smith, Female, Unknown => Ms. Smith 
#Helen Taylor, Female, Married => Mrs. Taylor

name=input("請輸入姓名:")
name=name[0].upper()+name[1:].lower()
#gender性別(Female女,Male男)
gerder=input("請輸入性別(M or F):").upper()
married=input("請問您結婚了嗎(Y/N):").upper()

#第三格式化(注意""及:)
if gerder == "F":
    if married == "Y":
        print("Mrs. %s"%(name))
    elif married == "N":
        print("Miss. %s"%name)
    else:
        print("Ms. %s"%name)
else:
    print("Mr. %s"%name)

#第二格式化
if gerder == "F":
    if married == "Y":
        print("Mrs.{:s}".format(name))
    elif married == "N":
        print("Miss.{:s}".format(name))
    else:
        print("Ms.{:s}".format(name))
else:
    print("Mr.{:s}".format(name))

#第一格式化
if gerder == "F":
    if married == "Y":
        print(f"Mrs.{name:s}")
    elif married == "N":
        print(f"Miss.{name:s}")
    else:
        print(f"Ms.{name:s}")
else:
    print(f"Mr.{name:s}")

#記得用,隔開不同類之物件
if gerder == "F":
    if married == "Y":
        print("Mrs.",name)
    elif married == "N":
        print("Miss.",name)
    else:
        print("Ms.",name)
else:
    print("Mr.",name)
"""

"""#99乘法表

for x in range(1,10):
    for y in range(1,10):
        #print(x,"x",y,"=",x*y)
        #print(f"{x:2d} x{y:2d} = {x*y:2d}")   #第一格式化
        #print("{:2d} x{:2d} = {:2d}".format(x,y,x*y))   #第二格式化.format是用.
        #print("%2d x%2d = %2d"%(x,y,x*y))  #第三格式化
"""

"""#檢查質數     #有用到for迴圈+break(停止)
#讓用戶輸入一個數值，檢查該數值是否為質數
#1.讓用戶輸入一個數 x
#2.利用for 迴圈從1逐一檢查到x
#3.如果有1和x之外的其他數，能夠整除ｘ則不是質數
x=int(input("請輸入一個質數:"))
if x > 1 :    #檢查 x 是否大於1，因為1和小於1的數字都不是質數
    for y in range(2,x):
        if x%y == 0 :
            print("輸入錯誤,",x,"非質數")
            break       #break(停止):用在迴圈中,達成條件及停止的用法
        else:
            print("輸入正確,",x,"是質數")
            break
else:print("1和小於1的數字都不是質數,請輸入大於1的數值!")
"""

"""#請用戶輸入一個100以內的數，並求出其因數     #有print()的end用法
#在 Python 中，print() 函數的 end 參數用於指定打印語句結束時的字符，默認值是換行符 \n。
# 這意味著每次調用 print() 函數時，輸出的內容會自動換行。
#通過使用 end=" "，你可以更改這個行為，使每次調用 print() 函數時，輸出不換行，而是在同一行繼續，
# 並在輸出的內容後面加上一個空格。這在打印多個項目並希望它們出現在同一行時特別有用。
#1.輸入一個數值 x
#2.利用while 迴圈，從1逐一遞增至 x
#3.檢查迴圈過程中每一個數，是否為 x的因數
#4.將因數逐一印出 
num=int(input("請輸入一個數值(1~100):"))
print(num,"的因數有:",end=" ")
tot=0
while tot <= num :
    tot += 1
    if num % tot == 0 :
        print(tot,end=",")

#下為用for迴圈解法
#num = int(input("Enter a number: "))
#print(num, "的因數有：", end=" ")  # 打印提示信息，不換行
#for x in range(1, num + 1):  # 使用 for 迴圈遍歷從 1 到 num 的所有數字
#    if num % x == 0:  # 如果 num 能被 x 整除
#        print(x, end=" ")  # 打印 x，並在後面加一個空格，保持輸出在同一行

"""

"""    #檢驗統一編號
#邏輯乘數12121241(代為y)
#統編=id

y="12121241"     
id=input("請輸入統編(8碼):")       
tot=0   #設定和數為0初始值
for x in range(len(id)):        #用for迴圈使x依序代入0~7,完成區塊內循環相加
    z = int(id[x])*int(y[x])    #取得id與羅輯乘數同位置之積
    w = f"{z:02d}"              #因驗證規則的原因將所有得到之積個位數於10為數位置補0,轉化為雙位數
    tot += (int(w[0])+int(w[1]))  #依驗證規則"兩數上下對應相乘,乘積直寫並上下相加,將相加之和在相加
if len(id) == 8 :               #如果長度為8
    if id[6] == "7" :           #如果id第七個號碼為7。驗證規則:如倒數第二位為7,乘積直寫並上下相加,\
                                #   再相加時最後第二位數 分別取 0 or 1
        if (tot-10) % 5 == 0 or (tot-9) % 5 == 0 :      #因id第七位為7時會固定乘積為7*4=28
            print("您輸入的統編為:",id,"統編正確")       #依驗證規則會是2+8=10;以155~158會於代入時加上2再加8,共10
        else : print("您輸入的統編為:",id,"統編驗證失敗,為無效統編")    #規則為 0 or 1 ;所以偷吃步用(10-10)=(+0)
                                                                                                #(10-9)=(+1)
    else : 
        if tot % 5 == 0 :       #到數第二位不為7,算後總和能讓5整除,正確
            print("您輸入的統編為:",id,"統編正確")
        else : 
            print("您輸入的統編為:",id,"統編驗證失敗,為無效統編")      #算後總和不能讓5整除,錯誤
else : print("查無資料,請正確輸入8位數統一編號")    #長度不為8,錯誤
"""
