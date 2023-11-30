import sqlite3

class Baza():
    def __init__(self):
        self.conn=sqlite3.connect('name.db')
        self.cursor = self.conn.cursor()
    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
            self.conn.commit()
            print('Вы создали таблицу')
        except:
            print('Таблица уже существует')


p=Baza()
v=Baza()
p.create_table()
v.create_table()