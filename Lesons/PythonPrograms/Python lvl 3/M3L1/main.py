import sqlite3 
con = sqlite3.connect("tutorial.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5),
        ('Friends', 2004, 10.0)
""")
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)
con.close()