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
    text = row[0]
    user_name = row[1]
    parent_id = row[2]
    longiture = row[3]
    latutide = row[4]
    temperature = round(row[5])
    city = row[6]
    
    
    #Current date and time formatted as YYYY-MM-DD HH:MI
    dttm = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    #Prepare new row to insert into table
    new_row = (text, user_name, dttm, parent_id, longiture, latutide, temperature, city)
    
    #Temporary instance "g" to connect with DB
    cursor = connection_db()
    cursor.execute("insert into comments (text, username, dttm, parentid, longiture, latutide, temperature, city)"\
                   " values (?, ?, ?, ?, ?, ?, ?, ?)", new_row)
    cursor.commit()
    cursor.close()


#Return all comments from the table
def select_all_comments():

    #select all comments
    cursor = connection_db()
    records = cursor.execute("select text, username, dttm from comments")

    #Convert records to dictionary
    posts = [{'text' : str(row[0]),
        'username' : str(row[1]),
        'datetime' : str(row[2])
    } for row in records.fetchall()]

    cursor.close()
    
    return posts


#Return all comments and responses (child comments)
def select_all_comments_and_responses():

    #Creating query string
    #Return all field and level of comment (depth = textlevel)
    query_string =  "WITH RECURSIVE commenttree AS "
    query_string = query_string + "(SELECT rowid, text, username, dttm, parentid, longiture, latutide, temperature, "
    query_string = query_string + "city, dttm||rowid As item_path "
    query_string = query_string + "FROM comments "
    query_string = query_string + "WHERE parentid IS NULL or parentid = 0 "
    query_string = query_string + "UNION ALL "
    query_string = query_string + "SELECT child.rowid, child.text, child.username, child.dttm, child.parentid, "
    query_string = query_string + "child.longiture, child.latutide, child.temperature, child.city, "
    query_string = query_string + "tree.item_path||'->'||child.dttm||child.rowid As item_path "
    query_string = query_string + "FROM comments As child "
    query_string = query_string + "INNER JOIN commenttree AS tree "
    query_string = query_string + "ON (child.parentid = tree.rowid) "
    query_string = query_string + ") "
    query_string = query_string + "SELECT rowid, text, username, dttm, longiture, latutide, temperature, city, "
    query_string = query_string + "(length(item_path) - length(replace(item_path,'->', ' ')) +1) as textlevel "
    query_string = query_string + "FROM commenttree "
    query_string = query_string + "ORDER BY item_path"

    #open connection with DB
    cursor = connection_db()
    records = cursor.execute(query_string)

    #Charset
    charset = "utf-8"

    #Convert records to dictionary
    posts = [{'postid' : str(row[0]),
        'text' : str(row[1]),
        'username' : str(row[2]),
        'datetime' : str(row[3]),
        'longitude' : str(row[4]),
        'latitude' : str(row[5]),
        'temperature' : str(row[6]),
        'city' : str(row[7]),
        'textlevel' : row[8]
    } for row in records.fetchall()]
    
    cursor.close()
    
    return posts


