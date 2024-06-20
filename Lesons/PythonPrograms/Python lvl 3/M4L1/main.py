import sqlite3 

database = 'movie.db'

connection = sqlite3.connect(database)

cursor = connection.cursor()


cursor.execute('''
               SELECT * FROM movies
WHERE director_id IN (4765, 5417);''')

result = cursor.fetchall()
connection.close()

for row in result:
  print(row)