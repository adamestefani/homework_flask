from flask import Flask, render_template, request, jsonify
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from HTMLParser import HTMLParser


#start the app
app = Flask(__name__)

#Set certificate
context = ('server.crt', 'server.key')


#first page
@app.route('/comment', methods=['GET'])
def comment():
    return render_template('index.html')


#see comment
@app.route('/allcomment', methods=['POST'])
def allcomment():

    charset = 'utf-8'

    #Data sent by html form
    new_text = request.form['textInput'].encode(charset)
    new_user_name = request.form['userName'].encode(charset)
    new_parent_id = request.form['parentId']
    new_city = request.form['city'].encode(charset)
    

    #Prevent HTML tags from the form
    new_text = strip_tags(new_text)
    new_user_name = strip_tags(new_user_name)
    new_city = strip_tags(new_city)


    #Verify parameters
    if (new_parent_id == None or new_parent_id == ''):
        new_parent_id = '0'


    #Calling REST
    #Request string
    request_string = 'https://localhost:8080/text/'+new_text+ \
        '/user/'+new_user_name+'/parentid/'+new_parent_id+'/city/'+new_city
    
    #Disable warnings (internal call)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    #Call internal service
    response_text = requests.get(request_string, verify=False)
    
    return response_text.text
    

#Class to prevent HTML tags -- Begin
class StripTags(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = StripTags()
    s.feed(html)
    return s.get_data()
#Class to prevent HTML tags -- End



#run app
if __name__ == "__main__":

    app.run(host='127.0.0.1', port=5000, ssl_context=context, threaded=True, debug=True)
