import csv
import datetime

from db import User, Post, db_session
posts_list = []
u = User

with open('example.csv', 'r', encoding = 'utf8') as f:
	fields = ['title', 'published', 'content', 'email', 'first_name', 'last_name']
	reader = csv.DictReader(f, fields, delimiter= ',')
	for row in reader:
		row['published'] = datetime.datetime.strptime(row['published'], '%d.%m.%y %H:%M')
		author = u.query.filter(User.email == row['email']).first()
		row['user_id'] = author.id
		posts_list.append(row)

for post_data in posts_list:
	post = Post(post_data['title'], posts_data['published'], post_data['content'], posts_data['user_id'])
	db_session.add(post)

	db_session.commit()