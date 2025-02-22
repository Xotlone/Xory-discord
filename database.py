import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()

Member = cursor.execute('CREATE TABLE IF NOT EXISTS "Member"(ID, Score)')

db.close()