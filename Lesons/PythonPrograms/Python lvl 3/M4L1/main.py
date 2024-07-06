import sqlite3 

database = 'movie.db'

connection = sqlite3.connect(database)

cursor = connection.cursor()

# cursor.execute('''
#                 SELECT MAX(budget),title FROM movies
# ''')
# cursor.execute('''
#                SELECT title,MAX(budget),popularity,release_date FROM movies WHERE release_date = 2009-12-10''')

# cursor.execute('''
#                SELECT title,budget,MAX(popularity),release_date FROM movies ''')

# cursor.execute('''
#                 SELECT * FROM movies WHERE budget > 30000000 AND director_id = 5417
# ''')
# cursor.execute('''
#                 SELECT "The battle within." FROM movies 
# ''')
# cursor.execute('''SELECT title,budget,popularity,release_date FROM movies WHERE title = The battle within.''')

# cursor.execute('''
#                SELECT title,budget,popularity,release_date,vote_average,vote_count FROM movies GROUP BY release_date HAVING release_date < 1980 AND vote_count > 8''')

# cursor.execute('''
#         SELECT title, budget FROM movies ORDER BY popularity DESC LIMIT 1;
# ''')

# cursor.execute('''
#           SELECT title, buget FROM moives WHERE release_date LIKE "2009-12%" ORDER BY budget DESC LIMIT 1;
# ''')

# cursor.execute('''
#             SELECT * FROM movies WHERE tagline = "The battle within.";
# ''')

# cursor.execute('''
#             SELECT * FROM movies WHERE release_date < 1980 and vote_average > 8 ORDER BY vote_count DESC LIMIT 1;
# ''')

# cursor.execute('''
#               SELECT title,budget,popularity,MAX(release_date),vote_average,vote_count,director_id FROM movies WHERE director_id = 4762''')

cursor.execute('''
              SELECT title,budget,popularity,release_date,COUNT(tagline),director_id FROM movies WHERE director_id = 4762''')

result = cursor.fetchall()
connection.close()

for row in result:
  print(row)