from flask import Flask

app = Flask(__name__)

@app.route('/test')
def index():
	return "Hello world!"


if __name__ == '__main__':
	app.run()