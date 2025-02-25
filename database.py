import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

Member = cursor.execute('CREATE TABLE IF NOT EXISTS "Member"(ID, Score)')