import sqlite3

with sqlite3.connect("homework.db") as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE comments (text varchar(500), dttm varchar(20))")
