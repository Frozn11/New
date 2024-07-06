import sqlite3


database = 'world_information.db'

connection = sqlite3.connect(database)

cursor = connection.cursor()


# cursor.execute('''
#               SELECT country,capital FROM country WHERE country = "Самоа" ''')

# cursor.execute('''
#               SELECT COUNT(continent) FROM continents ORDER BY continent''')

## area

## country_id

# cursor.execute('''
#               SELECT country,MIN(area) FROM info JOIN country ON info.country_id = country.country_id''')

# cursor.execute('''
#                 # SELECT country,MAX(density) FROM info JOIN country ON info.country_id = country.country_id''')

# cursor.execute('''
#                 SELECT continents.continent FROM info JOIN country ON info.country_id == country.country_id JOIN continents ON continents.continent_id == country.continent_id WHERE country.capital == "Бастер"''')

# cursor.execute('''
#                 SELECT count(*) FROM country JOIN continents ON continents.continent_id == country.continent_id WHERE continents.continent == "Африка" ''')

# cursor.execute('''
#                 SELECT country,MAX(population) FROM info JOIN country ON info.country_id = country.country_id WHERE population = 1500001''')

# cursor.execute('''
#                 SELECT country,MAX(population) FROM info JOIN country ON info.country_id = country.country_id WHERE population > 10000000 AND area < 80000000''')

# cursor.execute('''
#                 SELECT * from country
# WHERE country.capital LIKE "Б%"; ''')

# cursor.execute('''
#                 SELECT continent, avg(density) FROM info
# JOIN country ON info.country_id == country.country_id
# JOIN continents ON continents.continent_id == country.continent_id
# GROUP BY country.continent_id
# ORDER BY avg(density); ''')

# cursor.execute('''
#                 SELECT population, capital FROM info
# JOIN country ON info.country_id == country.country_id
# WHERE info.percentage == 0; ''')

# cursor.execute('''
#                 SELECT country FROM info
# JOIN country ON info.country_id == country.country_id
# WHERE country.continent_id == 4 and country LIKE "%ия"
# ORDER BY population
# LIMIT 1; ''')

cursor.execute('''
                SELECT avg(population) FROM info
JOIN country ON info.country_id == country.country_id
JOIN continents ON continents.continent_id == country.continent_id
WHERE continent == "Европа"
ORDER BY density
LIMIT 10; ''')


result = cursor.fetchall()
connection.close()

for row in result:
  print(row)