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


def del_and_update():
    c.execute("SELECT * FROM posts ")
    [print(row) for row in c.fetchall()]
    
 #   print('=================After  update===========')
 #   c.execute('UPDATE posts SET value =100 WHERE value = 9')
 #   conn.commit()
 #   c.execute("SELECT * FROM posts ")
 #   [print(row) for row in c.fetchall()]

    c.execute('DELETE FROM posts WHERE value == 100')
    conn.commit()
    print('=================After  Delete ===========')

    c.execute('SELECT *FROM posts')
    [print(row) for row in c.fetchall()]








del_and_update()


#create_table()
#for i in range(10):
#   dynamic_data_entry()
#   time.sleep(1)

c.close()
conn.close()


#create_table()
#data_entry()
