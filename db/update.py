import sqlite3

class Database:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (col_1 INT PRIMARY KEY UNIQUE, col_2 TEXT)''')
    conn.commit()
    
    def __init__(self,id,value):
        self.value=value
        if isinstance(id,int) and id>-1:
            self.id=id
        else:
            print('id должен быть числом')
            exit()
            
    def new_value(self): 
        try:
            if isinstance(self.value,str):
                self.cursor.execute('''INSERT INTO mytable (col_1,col_2) VALUES (?,?)''', (self.id,self.value,))
                print('Вы сделали запись в таблице')
            else:
                print('Значение должно быть текстом')
        except:
            print('Такой id уже существует')

    def up(self): 
        self.cursor.execute('''UPDATE mytable SET col_2=(?) WHERE col_1=(?)''', (self.value,self.id))

    def proverka(self):
        self.cursor.execute('''SELECT * FROM mytable''')
        k = self.cursor.fetchall()
        print(k)

p=Database(1,'raz')
t=Database(2,'dva')
v=Database(1,'new value')
#r=Database(3,4)
#u=Database('vvv','bbb')
p.new_value()
t.new_value()
v.new_value()
#r.new_value()
v.up()
t.proverka()
