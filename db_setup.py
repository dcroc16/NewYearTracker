import sqlite3

db = sqlite3.connect('backend.db')

c = db.cursor()

c.executescript('''
	CREATE TABLE weight (
	id integer primary key autoincrement,
	date datetime,
	weight float

	)

		''')

db.commit()

db.close()

