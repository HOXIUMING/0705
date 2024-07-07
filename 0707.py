#讓用戶輸入姓名當日氣溫，18度以下顯示”寒冷”，18~30度顯示”舒適”，30度以上顯示”炎熱”
#name=input("請問您的大名是:")
#temperatture氣溫
#temperatture=float(input("現在溫度是:"))
"""第三格式化
if temperatture < 18 :
    print("您好%s,現在溫度是%d度,是寒冷的,注意保暖!"%(name,int(temperatture)))
elif temperatture < 30 :
    print("您好%s,現在溫度是%d度,是舒適的,祝您今日愉快!"%(name,int(temperatture)))
else:print("您好%s,現在溫度是%d度,是炎熱的,請多補充水分!"%(name,int(temperatture)))
""" 
"""第二格式化
if temperatture < 18 :
    print("您好{:s},現在溫度是{:d}度,是寒冷的,注意保暖!".format(name,int(temperatture)))
elif temperatture < 30 :
    print("您好{:s},現在溫度是{:d}度,是舒適的,祝您今日愉快!".format(name,int(temperatture)))
else:print("您好{:s},現在溫度是{:d}度,是炎熱的,請多補充水分!".format(name,int(temperatture)))
"""
"""第一格式化
if temperatture < 18 :
    print(f"您好{name:s},現在溫度是{int(temperatture):d}度,是寒冷的,注意保暖!")
elif temperatture < 30 :
    print(f"您好{name:s},現在溫度是{int(temperatture):d}度,是舒適的,祝您今日愉快!")
else:print(f"您好{name:s},現在溫度是{int(temperatture):d}度,是炎熱的,請多補充水分!")
"""
#讓用戶依序輸入姓名、性別、婚姻狀態，並依顯示其尊稱Miss，Mrs，Ms，Mr 及其姓名。
#例：Angle Novak, Female, Not married => Miss Novak
#Cindy Connor, Male, Married => Mr. Connor
#Emma Smith, Female, Unknown => Ms. Smith 
#Helen Taylor, Female, Married => Mrs. Taylor
name=input("請輸入姓名:")
name=name[0].upper()
#gender性別
gerder=input("請輸入性別(M or F):")
married=