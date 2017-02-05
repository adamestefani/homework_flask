from flask import Flask
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.database = "homework.db"

#Create a connection with DB
def connection_db():
    return sqlite3.connect(app.database)


#Insert a row into comments table
def insert_new_comment(row):
    
    #Parameter "row" is an array of fields
    # 0 = text
    text = row[0]
    
    #Current date and time formatted as YYYY-MM-DD HH:MI
    dttm = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    #Prepare new row to insert into table
    new_row = (text, dttm)
    
    #Temporary instance "g" to connect with DB
    cursor = connection_db()
    cursor.execute("insert into comments values (?, ?)", new_row)
    cursor.commit()
    cursor.close()
