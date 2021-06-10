from flask import Flask

from req import get_weather

from datetime import datetime

import settings

city_id = 524901
apikey = settings.API_KEY

app = Flask(__name__)

@app.route('/')
def index():
	url ='http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&appid=%s' % (city_id, apikey)
	weather = get_weather(url)
	cur_date = datetime.now().strftime('%d.%m.%Y')

	result = '<p><b>Temp:</b> %s</p>' % weather['main']['temp']
	result += '<p><b>City:</b> %s</p>' % weather['name']
	result += '<p><b>Date:</b> %s</p>' % cur_date


	return result

# run func
if __name__ == '__main__':
	app.run(debug=True)