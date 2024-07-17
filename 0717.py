#類別
"""
class person :                                      #class 類別
    name   = None                                   #屬性>>變數 = ____
    gender = None                                   #同上
    bday   = None                                   #同上

    def __init__(self, na, gd, bd) -> None:         #建構式
        print("Hello")

    def getTitle(self) :
        print("Title")

obj1 = person("NCHU", "F", "2000/01/01")
"""
"""
class person :                                      #class 類別
    name   = None
    gender = None
    bday   = None

    def __init__(self, na, gd, bd) -> None:
        self.name   = na
        self.gender = gd
        self.bday   = bd
        
    def getTitle(self) :
        if self.gender == "M" :
            print(f"Mr. {self.name}")
        else :
            print(f"Mis. {self.name}")

#繼承(這邊是繼承至[類別 person])
class stud(person) :
    #擴充(增加需要的功能)
    def getAge(self) -> int :                       #可設定資料類型,如此列的 int
        byy = int(self.bday[:4])
        return 2024 - byy
"""
"""
#繼承(這邊是繼承至[類別 stud])
from datetime import datetime
class member(stud) :
    #改寫:把現有的功能做調整
    def getAge(self) -> int:
        tyy = datetime.now().year
        tmd = datetime.now().strftime("%m%d")
        byy = int(self.bday[:4])
        bmd = self.bday[5:]
        if bmd  >= tmd : 
            return tyy - byy - 1                   #不足歲
        else :
            return tyy - byy                       #足歲
        

obj1 = person("NCHU", "F", "2000/01/01")
print(obj1.name)
obj1.getTitle()

obj2 = person("Sam", "M", "2000/01/01")
print(obj2.name)
obj2.getTitle()

obj3 = stud("Python", "M", "2000/12/31")
obj3.getTitle()
print(obj3.getAge())

obj4 = member("Python", "F", "2000/01/01")
obj4.getTitle()
print(obj4.getAge())
"""
"""
#繼承(這邊是繼承至[類別 person])
from datetime import datetime
class member(stud) :
    #擴充屬性
    id = None
    #部分改寫:把現有的功能做調整
    def __init__(self, na, gd, bd, id) -> None:
        super().__init__(na, gd, bd)
        self.id = id
    #全面改寫
    def getAge(self) -> int:
        tyy = datetime.now().year
        tmd = datetime.now().strftime("%m%d")
        byy = int(self.bday[:4])
        bmd = self.bday[5:]
        if bmd  >= tmd : 
            return tyy - byy - 1                   #不足歲
        else :
            return tyy - byy                       #足歲

obj5 = member("Python", "F", "2000/07/18","123")
obj5.getTitle()
print(obj5.getAge())
"""
"""
#匯入函式庫
import sqlite3
#連接資料庫
conn = sqlite3.connect("data.db")
#產生Cursor指標
curs = conn.cursor()
#資料查詢
curs.execute("SELECT * FROM MOCK_DATA WHERE id <= 5")
#印出欄位
print(curs.description)
#印出資料內容
print(curs.fetchall())
"""

#匯入函式庫
import sqlite3
class dSet :
    _conn   = None
    columns = None
    results = None
    isdebug = False

    def __init__(self,dbna : str, debug = False) -> None :
        self.__conn = sqlite3.connect(dbna)
        self.isdebug = debug

    def Query(self,sql : str) :
        if self.isdebug :
            print(sql)
        #----
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        self.columns = [col[0] for col in cursor.description]
        self.results = cursor.fetchall()
        #print(self.columns)
        #print(self.results)

    def Update(self,sql : str, *args) :
        cursor = self.__conn.cursor()
        cursor.execute(sql, args)
        self.__conn.commit()

    def getRowCount(self) :
        if self.columns == None or self.results == None :
            return None
        else :
            return len(self.results)

    def getValue(self, row : int, col : int) :
        if self.columns == None or \
           self.results == None or \
           row < 0 or \
           row >= self.getRowCount() :
            return None
        else :
            return self.results[row][col]

#obj = dSet("data.db")
#obj.Query("SELECT * FROM MOCK_DATA WHERE id <= 15")
"""#改資料庫內容
obj.Update("UPDATE MOCK_DATA SET first_name = ?, \
                                 last_name = ?,  \
                                 email =? \
                                 WHERE id = ?", \
                                 "XiuMing","HO","thgbvf19@gmail.com",1)
#WHERE id = ?前不能有 , 分開。因為更改first_name,last_name,email是在id第1行
"""
#print(obj.getRowCount())
#print(obj.getValue(9, 2))

class dateSet(dSet) :
    def getColumnIndex(self, colna : str) :
        if   self.columns == None :
            return None
        elif colna not in self.columns :
            return False
        else :
            return self.columns.index(colna)
        
    def getColumnValue(self, row: int, colna: str) :
        return self.getValue(row, self.getColumnIndex(colna))
    
    def getValue(self, row : int, col : int) :
        if col < 0 or col >= len(self.columns) :
            return None
        else :
            return super().getValue(row, col)
    
    def Query(self, sql: str):
        if sql.upper().strip().startswith("SELECT") :
            return super().Query(sql)
        else :
            self.columns = None
            self.results = None

    def Update(self, sql: str, *args):
        if not sql.strip().lower().startswith("select"):
            return super().Update(sql, *args)
        else :
            print("SQL Command Error!")

obj = dateSet("data.db", True)
obj.Query("SELECT * FROM MOCK_DATA WHERE id <= 15")
#print(obj.getColumnIndex("email"))
print(obj.getColumnValue(8, "gender"))