# Trying to work with data types

# Trying with numbers
import math
a = 4
math.sqrt(a)
math.sin(a)

b = 3.14
c = 3.67
round(b)
round(c)
math.floor(b)
math.floor(C)
math.cell(b)
math.cell(c)

# Trying with strings
a = 'hello'
print(a)
a.upper()
a = 'HELLO'
a.lower()
a = 'hello'
a.capitalize()
a.replace('l','a')

# Trying with list
a = 'learn.python.com'
a.split('.')

# Trying with formatting
a = 22
b = 'I am '
message = b + str(a)

a = 22
b = 1998
message = 'I am {}. I was born in {}.'.format(a,b)
message

#Trying with list
a = [1, 6, 8, 5, 2]
a[0]
a[2:4] #last symbol was not printed
a.append(99)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c.reverse()
c.sort()

# Trying with vocabulary
catalog_item = {
	"type":"phone",
	"vendor":"Apple"
}

catalog_item['audio_jack'] = False
print(catalog_item)
print(catalog_item['type'])

item_name = catalog_item['type'] + ' '+catalog_item['vendor']
print(item_name)
print(catalog_item.get('price'))
print(catalog_item.get('Discount','Скидок нет!'))
model in catalog_item
model not in catalog_item
del catalog_item['price']

# Trying with logic
if age < 18:
	print('You cant drink')
else:
	print('You can drink')

if not is_user_banned:
	ban_user(user)

if team == 'mystic':
	print('hi blue team!')
elif team == 'instinct':
	print('hi yellow team!')
elif team == 'valor':
	print('hi red team!')

if team == 'mystic':
	if user_level >=5:
		print('Welcome to the gym')
	else:
		print('Get more exp')


students_score = [1, 2, 3]
for score in students_score:
	print(score)

x = 1
while x < 5:
	print(x)
	x += 1

while True:
	user_say = input('Say something: ')
	if user_say == 'Bye':
		print('Okey, bye')
		break
	else:
		print('You are wonderful!')

# Trying with exceptions
def cut_cake(parts):
	try:
		return 1/int(parts)
	except (ZeroDivisionError, TypeError, ValueError):
		return('No no no!')

cake = cut_cake(0)
print(cake)

# Trying with modules
import datetime
datetime.datetime.now()	#Module.function.function
datetime.date.today()
datetime.timedelta(days = 231, seconds=35475, microseconds=765859)

date = datetime.datetime.now()
date.strftime('%d.%m.%Y %H:%M')
date.strftime('%A %d %B %m.%Y %H:%M') # For Mondays and Marchs

date_str = '12/23/2010'
date_s = datetime.strptime(date_str, '%m/%d/%Y')

# Third party import
pip3 list
pip3 install ephem
import ephem
mars = ephem.Mars('2016/09/23')
ephem.constellation(mars)

from telegram import Updater

# Trying with venv
pip install venv
# Should do in current location
python -m venv env
# e:\home\python\project\env\Scripts\activate.bat
# Command line starts with (env)
pip install flask
import flask
# e:\home\python\project\env\Scripts\deactivate.bat

# Trying with files
# Writing and rewriting
with open('text.txt', 'w', encoding='utf-8') as myfile:
	myfile.write("Hi!")

# Reading
with open('text.txt', 'r', encoding='utf-8') as myfile:
	contex = myfile.read()
	print(contex)
# But better use this
with open('text.txt', 'r', encoding='utf-8') as myfile:
	for line in myfile:
		line = line.uper()
		line = replace('\n', '')
		print(line)

# Add in the end of file
with open('text.txt', 'a', encoding='utf-8') as myfile:
	myfile.write("I am Grut\n\t")

#CSV Comma Separated Values
import csv
with open('data_usdrub.csv', 'r', encoding='utf-8') as f:
	fields = ['number', 'time', 'course']
	reader = csv.DictReader(f, fieldnames=fields, delimiter=';')
	for row in reader:
		print(row)

with open('data_usdrub.csv', 'w', encoding='utf-8') as f:
	fields = ['number', 'time', 'course']
	writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
	writer.writeheader()
	for course in course_list:
		writer.writerow(course)