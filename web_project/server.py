from flask import Flask, request

from req import get_weather

from datetime import datetime

import settings

city_id = 524901
apikey = settings.API_KEY

app = Flask(__name__)

@app.route('/news')
def all_the_news():
	colors = ['green', 'red', 'blue', 'magenta']
	try:
		limit = int(request.args.get('limit'))
	except:
		limit = 10
	color = request.args.get('color') if request.args.get('color') in colors else 'black'
	return '<h1 style="color: %s">News: %s </h1>' % (color, limit)

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