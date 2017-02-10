import requests

def info(city):

	#App key to request info
	APP_KEY = '498525eb5c13f7db3a855b31018118a9'
	app_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+ \
		'&units=metric&appid='+APP_KEY

	#Call weather app
	response_app = requests.get(app_url)

	#Verify response code = success
	if response_app.status_code == 200:

		#Convert response to JSON
		json_info = response_app.json()

		#Get specific info
		latitude = json_info['coord']['lat']
		longitude = json_info['coord']['lon']
		temperature = json_info['main']['temp']

	
	#Return a dictionary
	return (dict(latitude=latitude, longitude=longitude, temperature=temperature))
