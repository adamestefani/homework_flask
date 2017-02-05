from flask import Flask, request, jsonify
import dbcontroller


#start the app
app = Flask(__name__)

#rest to receive and return the same text
@app.route('/text/<string:text>', methods=['GET'])
def return_text(text):
    
    #Insert new comment into DB
    #Parameter must be an array of fields
    dbcontroller.insert_new_comment([text])
    
    
    #return text as JSON
    return jsonify({'text' : text})


#run app
if __name__ == "__main__":
    app.run(debug=True, port=8080)


