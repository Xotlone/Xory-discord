import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

member = cursor.execute('CREATE TABLE IF NOT EXISTS "Member"(ID, Score)')