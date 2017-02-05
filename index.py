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
    
    #Calling REST
    response_text = requests.get('http://localhost:8080/text/'+new_text+'/user/'+new_user_name)
    #print('response REST --- '+response_text.text)
    
    return response_text.text
    

#run app
if __name__ == "__main__":
    app.run(debug=True)
