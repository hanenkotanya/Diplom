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
    def sel(self):
        self.cursor.execute('''SELECT * FROM mytable''')
        k = self.cursor.fetchall()
        print(k)

v=Database()
v.sel()