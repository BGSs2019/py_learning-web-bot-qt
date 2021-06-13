from db import db_session, User

authors = [
	{
	'first_name': 'Vasya',
	'last_name' : 'Petrov',
	'email' : 'Vasya@example.com',
	},
	{
	'first_name': 'Misha',
	'last_name' : 'Ivanov',
	'email' : 'mari@example.com',
	},
	{
	'first_name': 'Hello',
	'last_name' : 'World',
	'email' : 'world@example.com',
	}
]

for a in authors:
	author = User(a['first_name'], a['last_name'], a['email'],)
	db_session.add(author)

	db_session.commit()