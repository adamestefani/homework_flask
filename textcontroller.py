from flask import Flask, request, jsonify
import dbcontroller


#start the app
app = Flask(__name__)

#rest to receive and return the same text
@app.route('/text/<string:text>', methods=['GET'])
@app.route('/text/<string:text>/user/<string:user_name>', methods=['GET'])
def return_text(text, user_name):
    
    #Insert new comment into DB
    #Parameter must be an array of fields
    dbcontroller.insert_new_comment([text, user_name])
    
    posts = dbcontroller.select_all_comments()
    
    #return text as JSON
    return jsonify({'posts' : posts})

#run app
if __name__ == "__main__":
    app.run(debug=True, port=8080)


