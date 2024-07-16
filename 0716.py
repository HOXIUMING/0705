"""#製作一個函式傳入一個整數num,計算1+num的總和
def getSum(num) :                                           #自定義 getSum 函式
    tot = 0
    for x in range(1, num+1) :
        tot += x
    print(f"The total from 1 to {num} = {tot}")

getSum(100)
"""

"""#製作一個函式傳入一個整數num,回傳所有的因數&製作一個函式傳入一個整數num,回傳該數值是否為質數
def getFactors(num) :
    f = []
    for n in range(1,num+1) :
        y = num // n 
        if y < n :
            break
        if num % n == 0 :
            f.append(n)
            if y != n :
                f.append(y)
    f.sort()
    return f
#print(getFactors(16))

#製作一個函式傳入一個整數num,回傳該數值是否為質數
def isPrime(num) :
    return len(getFactors(num)) == 2

#print(isPrime(13))

#製作一個函式傳入一個整數num,回傳第num個質數
def getPrimt(num) :
    cnt = 0 
    while num > 0 :
        cnt = cnt + 1
        if isPrime(cnt) :
            num = num - 1
    return cnt

#print(getPrimt(2))

#製作一個函式傳入N個整數,回傳其平均值
def getAvg(*args) :                             #打 * 號,代表能讓一個變數能輸入多個值
    tot = 0
    for n in args :
        tot = tot + n
    return tot / len(args)

print(getAvg(1,3,5,7,9,7))
"""

"""#製作一個函式傳入(身高,體重,性別),回傳BMI及標準對應
def getBMI(h,w,g="M") :
    BMI = w / (h ** 2)
    BMI_min = 20 if g.upper() == "M" else 18
    BMI_max = 25 if g.upper() == "M" else 22
    if   BMI < BMI_min :
        print(f"BMI = {BMI}, 過輕")
    elif BMI < BMI_max :
        print(f"BMI = {BMI}, 過重")
    else :
        print(f"BMI = {BMI}, 標準")
        
getBMI(1.73,65)                     #省略部分參數用內定值取代
getBMI(g="F",h=1.73,w=65)           #指定對應引數名稱,忽略其順序
"""

"""#製作一個函式傳入任意數量的Key & value 參數
def keyFun(**k) :                                               #會以字典的形式包裝資料
    print(k)

keyFun(a=1, b=2, c="3", d="ABCD")
keyFun(a=1, b=2, c="3", d="ABCD", e="姓名", f="出生日")
"""

#製作一個可以計算任意散行面積的Lambda
a = lambda r, d, p = 3.14 : r * r * p * (d / 360)               #r=半徑, d=圓心角, p=圓周率
print(a(10,360))


#製作一個函式,依用戶指定R/T/C(矩形.三角形.圓形),回傳對應形狀面積計算的Lambda
def getAreaLambda(s = "R") :                                    #無輸入形狀的話,內定為R(矩形)
    if s.upper() == "R" :
        return lambda w, h : w * h                              #矩形面積:底 w * 高 h
    elif s.upper() == "T" :
        return lambda b, h : b * h / 2                          #
    elif s.upper() == "C" :
        return lambda r, p = 3.14 : r * r * p
    else :
        return None
    
a = getAreaLambda("C")
print(a(10))