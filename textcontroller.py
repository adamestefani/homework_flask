from flask import Flask, request, jsonify
import dbcontroller
import weather


#start the app
app = Flask(__name__)

#Set certificate
context = ('server.crt', 'server.key')


#rest to receive and return the same text
@app.route('/text/<string:text>', methods=['GET'])
@app.route('/text/<string:text>/user/<string:user_name>', methods=['GET'])
@app.route('/text/<string:text>/user/<string:user_name>/parentid/<int:parent_id>', methods=['GET'])
@app.route('/text/<path:text>/user/<path:user_name>/parentid/<int:parent_id>/city/<path:city>', methods=['GET'])
def return_text(text, user_name=None, parent_id=0, city=None):
    
	#Get weather info
    if (city != None):
        response_weather = weather.info(city)
        longitude = response_weather['longitude']
        latitude = response_weather['latitude']
        temperature = response_weather['temperature']
        city_name = response_weather['city_name']


    #Insert new comment into DB
    #Parameter must be an array of fields
    dbcontroller.insert_new_comment([text, user_name, parent_id, longitude, latitude, temperature, city_name])
    
    posts = dbcontroller.select_all_comments_and_responses()
    
    #return text as JSON
    return jsonify({'posts' : posts})

#run app
if __name__ == "__main__":
    
    app.run(host='127.0.0.1', port=8080, ssl_context=context, threaded=True, debug=True)


