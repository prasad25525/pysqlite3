import sqlite3
conn = sqlite3.connect('blog.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS posts(unix REAL,datestamp TEXT,keyword TEXT,value REAl)')

def data_entry():
    c.execute("INSERT INTO posts VALUES(145262627,'2019-2-10','Python',25)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()