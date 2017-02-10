import sqlite3

with sqlite3.connect("homework.db") as connection:
    cursor = connection.cursor()
    cursor.execute("ALTER TABLE comments ADD COLUMN longiture  NUMERIC")
    cursor.execute("ALTER TABLE comments ADD COLUMN latutide  NUMERIC")
    cursor.execute("ALTER TABLE comments ADD COLUMN temperature  NUMERIC")
    cursor.execute("ALTER TABLE comments ADD COLUMN city  TEXT")
