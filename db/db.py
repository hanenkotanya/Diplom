import sqlite3

class Database:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE mytable (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
    conn.commit()
    cursor.execute('''INSERT INTO mytable (col_1) VALUES (1)''')
    cursor.execute('''INSERT INTO mytable (col_1) VALUES (2)''')
    conn.commit()
    def __init__(self):
        pass
    
    def deli (self):
        self.cursor.execute('''DELETE FROM mytable''')
        print('vce gud')
v=Database()
v.deli()