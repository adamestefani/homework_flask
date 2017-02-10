import sqlite3

with sqlite3.connect("homework.db") as connection:
    cursor = connection.cursor()
    cursor.execute("ALTER TABLE comments ADD COLUMN parentid INTEGER")
