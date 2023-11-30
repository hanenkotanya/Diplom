import sqlite3

class Database:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (col_1 INT PRIMARY KEY UNIQUE)''')
    conn.commit()
    
    def __init__(self):
        pass
    
    def new_value(self,id):
        try:
            if isinstance(id,int) and id>-1:
                self.id=id
            else:
                print('id должен быть числом')
                exit()   
            self.cursor.execute('''INSERT INTO mytable (col_1) VALUES (?)''', (self.id,))
            print('Вы сделали запись в таблице')
        except:
            print('Такой id уже существует')

    def proverka(self):
        self.cursor.execute('''SELECT * FROM mytable''')
        k = self.cursor.fetchall()
        print(k)

    def deli (self,id):
        self.id=id
        self.cursor.execute('''DELETE FROM mytable WHERE col_1 = (?)''',(self.id,))
        print('vce gud')

v=Database()
k=Database()
v.new_value(1)
k.new_value(2)
k.proverka()
v.deli(1)
k.proverka()