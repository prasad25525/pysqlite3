import sqlite3
import datetime
import time
import random

conn = sqlite3.connect('Blog.db')
c = conn.cursor()


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS posts(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')


def data_entry():
    c.execute("INSERT INTO posts VALUES(127282,'2019-01-09','Python',8)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO posts (unix,datestamp,keyword,value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM posts')
    #c.execute("SELECT * FROM posts WHERE value=5 AND datestamp >= '2019-02-10 11:50:47'")
    #c.execute("SELECT keyword,value from posts WHERE  value=5 AND datestamp >= '2019-02-10 11:50:47'")
    #data = c.fetchall()
   # print(data)
    for row in c.fetchall():
        print(row)


#create_table()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)

#data_entry()

read_from_db()
c.close()
conn.close()
