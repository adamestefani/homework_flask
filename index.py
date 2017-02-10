from flask import Flask, render_template, request, jsonify
import requests


#start the app
app = Flask(__name__)

#first page
@app.route('/comment', methods=['GET'])
def comment():
    return render_template('index.html')


#see comment
@app.route('/allcomment', methods=['POST'])
def allcomment():
    
    #Data sent by html form
    new_text = request.form['textInput']
    new_user_name = request.form['userName']
    new_parent_id = request.form['parentId']
    new_city = request.form['city']
    
    #Verify parameters
    if (new_parent_id == None or new_parent_id == ''):
        new_parent_id = '0'


    #Calling REST
    #Request string
    request_string = 'http://localhost:8080/text/'+new_text+ \
        '/user/'+new_user_name+'/parentid/'+new_parent_id+'/city/'+new_city
    
    response_text = requests.get(request_string)
    
    return response_text.text
    

#run app
if __name__ == "__main__":
    app.run(debug=True)
