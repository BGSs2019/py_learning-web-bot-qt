from flask import Flask, render_template, request

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
	return render_template('index.html')

@my_flask_app.route('/all')
def all():
	return render_template('all.html')	

@my_flask_app.route('/login/', methods=['POST'])
def login():
	return render_template('login.html', login=request.form.get('Admin'), password=request.form.get('00000000'))

if __name__=='__main__':
	my_flask_app.run(debug=True)