"""
第二格式化(老師自訂義,分辨用)
x=10
y="Sam"
print("The number{:5d}from{:10s}on{:s}".format(x*3,y,"Fed"))
"""

"""
第三格式化(老師自訂義,分辨用)
x=10
y="Sam"
print("The number %5d from %10s on %s"%(x*5,"07/05",y))
"""

"""
整合看
x=10
y="Sam"
print("The number{:5d}from{:10s}on{:s}".format(x*3,y,"Fed"))
print("The number %5d from %10s on %s"%(x*5,"07/05",y))
"""

"""
BMI計算
BMI:體重(kg)/身高(m)*身高
男性標準:20~25
女性標準:18~22
小於標準值顯示:多吃一點吧!
介於標準值顯示:保持得很棒!
大於標準值顯示:該運動了喔!
"""
"""
input(h)
      w
      g>男:M,女:F

float(H)
      W

BMI=W/H*H

IF男:
if低標:
elif高標:
else....

"""
"""

#輸入資料
h=input("身高(M): ")
w=input("體重(kg): ")
g=input("性別(男:M,女:F)")
#資料轉型
h=float(h)
w=float(w)
#資料處理
BMI=w/(h*h)
#資料輸出
if g=="M":
    if BMI< 20:
      print("BMI={:f},{:s}".format(BMI,"多吃一點吧!"))
    elif BMI>25:
      print("BMI={:f},{:s}".format(BMI,"該運動了喔!"))
    else:
      print("BMI={:f},{:s}".format(BMI,"保持得很棒!"))
      #print("{1:s},BMI={0:f}".format(BMI,"保持得很棒!"))也可以,只是順序調過來顯示(身高1.75體重63性別M)輸出=保持得很棒!,BMI=20.571429
else:
    if BMI<18:
      print("BMI={:f},{:s}".format(BMI,"多吃一點吧!"))
    elif BMI>22:
      print("BMI={:f},{:s}".format(BMI,"該運動了喔!"))
    else:
      print("BMI={:f},{:s}".format(BMI,"保持得很棒!"))

"""
#下為上之縮寫
"""

#輸入資料
h=input("身高(M): ")
w=input("體重(kg): ")
g=input("性別(男:M,女:F)")
#資料轉型
h=float(h)
w=float(w)
#資料處理
BMI=w/(h*h)
#資料輸出
bmi_mix=20 if g == "M" else 18
bmi_max=25 if g == "m" else 22
if g=="M":
    if BMI< bmi_mix:
      print("BMI={:f},{:s}".format(BMI,"多吃一點吧!"))
    elif BMI>bmi_max:
      print("BMI={:f},{:s}".format(BMI,"該運動了喔!"))
    else:
      print("BMI={:f},{:s}".format(BMI,"保持得很棒!"))

    print("BMI={:f},{:s}".format(BMI,"多吃一點吧!"if BMI< bmi_mix else "該運動了喔!" if elif BMI>bmi_max else "保持得很棒!")

"""
"""

XXXXX停車場收費方式如下
1.前15分鐘,免費
2.第一個小時40元
3.之後每30分鐘,20元
4.當日最高不超過160元
讓用戶輸入停車分鐘數

輸出:
停車(分) 優惠(分) 停車金額 應繳金額
-------- -------- -------- --------
12345678 12345678 12345678 12345678

"""
#m=input("輸入分鐘(m):")
#x=m//30*20
#y=40+x
#    if "y" >= 400 
#m=int(m)
#
#print("{:f}{:S}{:s}{:s}.format(m,,,)")
"""
#資料輸入
tm=input("停車時間(分):")
#資料轉型
tm=int(tm)
#資料處理
amt=0   #總金額
amt=int(amt)
pay=0   #應付金額
pay=int(pay)
tm=tm
#15~60分鐘
if tm > 15:
    amt=40
#超過60分鐘
if tm > 60:
    amt=amt+20*((tm-60)//30)
    if(tm-60)%30>0:
        amt=amt+20
if amt > 160:
    pay=160
#超過60分鐘
if tm > 60:
    amt=amt+20*((tm-60)//30)
    if(tm-60)%30>0:
        amt=amt+20
if amt > 160:
    pay=160
else:
    pay=amt

#輸出
#tm=停車間分(tm)
#amt=停車金額
#pay=應繳金額

print("停車(分) 優惠(分) 停車金額 應繳總額")
print("-------- -------- -------- --------")
print("%8d %8d %8d %8d"%(tm, 15 if tm > 15 else tm, amt, pay)) #第三格式化表示
print("{:8d}{:8d}{:8d}{:8d}".format(tm,0 if tm > 15 else tm,amt,pay)) #第二格式化表示

"""

#驗證身分證
#輸入=身分字號  id
#轉型=轉大寫
#資料處理=1.取出第一個字    id[0]
#        (2).if a
#            elif b
#            elif c
#            ........
#        2.ABCDEFGHIJKLMNOPQRSTUVWXYZ
#取出資料在字串中的位置     >>>     位置(P)=字位置=字串.index(內容)  
#        3.str(P+10)+id[1:]
#        4.

#p="0123456789"
#n=input("Enter a number:")
#print("The position at []".format(p.index(n)))

"""
輸入身分證號進行驗證
"""
"""

#輸入資料
id=input("請輸入身分證號:")     #文字
#資料轉型
id=id.upper()
#資料處理
fst="ABCDEFGHJKLMNPQRSTUVXYWZIO".index(id[0])   #>>>位置(數值)
nid=str(fst+10)+id[1:]      #>>>文字+文字=文字
tot=int(nid[0])*1+\         
    int(nid[1])*9+\
    int(nid[2])*8+\
    int(nid[3])*7+\
    int(nid[4])*6+\
    int(nid[5])*5+\
    int(nid[6])*4+\
    int(nid[7])*3+\
    int(nid[8])*2+\
    int(nid[9])*1           #nid(文字)轉數值加int(),才能做計算

r=tot%10
r=(10-r)%10
print("正確")if r == int(nid[10])else print("錯誤")

"""
"""
輸入電話號碼轉成國字大寫
"""
"""
#輸入>轉型>處理>輸出
c=零壹貳參肆伍陸柒捌玖
#輸入
tel=input("請輸入電話號碼:")
#資料轉型
No
#資料處理
num0=tel{0}     #文字

"""
"""

c="零壹貳參肆伍陸柒捌玖"
tel=input("請輸入電話號碼:")
ctel=c[int(tel[0])]+\
     c[int(tel[1])]+\
     c[int(tel[2])]+\
     c[int(tel[3])]+\
     c[int(tel[4])]+\
     c[int(tel[5])]+\
     c[int(tel[6])]+\
     c[int(tel[7])]+\
     c[int(tel[8])]+\
     c[int(tel[9])]
print("中文:",ctel)

"""
"""

tel=input("請輸入電話號碼:")
tel=tel.replace("0","零")
tel=tel.replace("1","壹")
tel=tel.replace("2","貳")
tel=tel.replace("3","參")
tel=tel.replace("4","肆")
tel=tel.replace("5","伍")
tel=tel.replace("6","陸")
tel=tel.replace("7","柒")
tel=tel.replace("8","捌")
tel=tel.replace("9","玖")
print(tel)

"""
"""

tel=input("請輸入電話號碼:")
#tel=tel.replace("0","零").replace("1","壹").replace("2","貳").replace("3","參").replace("4","肆").replace("5","伍").replace("6","陸").replace("7","柒").replace("8","捌").replace("9","玖")
print(tel)
#或把它分行,會比較好看
tel=tel.replace("0","零").\
         replace("1","壹").\
         replace("2","貳").\
         replace("3","參").\
         replace("4","肆").\
         replace("5","伍").\
         replace("6","陸").\
         replace("7","柒").\
         replace("8","捌").\
         replace("9","玖")

"""
"""

#也可這樣寫,速度不會比較快,但較省記憶體
tel=input("請輸入電話號碼").replace("0","零").\
                           replace("1","壹").\
                           replace("2","貳").\
                           replace("3","參").\
                           replace("4","肆").\
                           replace("5","伍").\
                           replace("6","陸").\
                           replace("7","柒").\
                           replace("8","捌").\
                           replace("9","玖")
print(tel)

"""
"""
for x in range(10):
    print(x)
"""
"""
0
1
2
3
4
5
6
7
8
9
"""
"""
for x in range(0,10):
    print(x)
"""
"""
0
1
2
3
4
5
6
7
8
9
"""
"""
for x in range(5,10):
    print(x)
5
6
7
8
9
"""
"""
for x in range(0,10,1):
    print(x)
0
1
2
3
4
5
6
7
8
9
"""
"""
for x in range(0,10,3):
    print(x)
0
3
6
9
"""
"""
s="ABCDEF"
for x in range(6):
    print(s[x])
    ???????????????????????????????????
"""
"""
#輸入一段文字,將內容大/小寫互換
s=input("請輸入字串:")
n=""
for x in range(len(s)):
    if s[x].upper()==s[x].lower():       #<<<此行先寫入會比較好,符合此行代表此字非英文
        n=n+s[x]
    elif s[x].upper()==s[x]:
        n=n+s[x].lower()
    else:
        n=n+s[x].upper()
print(n)
"""
s=input("請輸入字串:")
n=""
for x in range(len(s)):
    n=n+(s[x] if s[x].upper()==s[x].lower() else s[x].lower() if s[x].upper()==s[x]else s[x].upper())
    print(n)
