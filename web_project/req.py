import requests
import settings

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print("Something wrong =(")

if __name__ == '__main__':
	data = get_weather('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid={}'.format(settings.API_KEY))
	print(data)