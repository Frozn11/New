import sqlite3

conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS youtube_videos 
(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    video_url TEXT NOT NULL,
    author TEXT,
    release_date TEXT,
    description TEXT          
)
''')

videos = [
    (1, 'Lofi music', 'https://www.youtube.com/watch?v=axWcKL4Ztsg', 'Little Soul', '2024-04-18', 'Music for work'),
    (2, 'Долотовская', 'https://youtu.be/R1lNwZS6wz4?si=uPJ13A8s6np7d1y5', 'Дудь', '2024-04-15', 'Видео про обезьян'),
    (3, 'Rick Astley - Never Gonna Give You Up', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Rick Astley', '2009-09-25', 'Rick Astley'),
    (4, 'Hello', 'https://www.youtube.com/watch?v=aaIjs8K3oYo&list=PLYBtTW5LzKYctE0lMIl31EEqJWlsv-Xaa&index=11', 'OMFG1', '2015-03-21', 'Hello'),
    (5, 'My Ordinary Life-The Living Tombstone', 'https://youtu.be/9Zj0JOHJR-s?si=MQyeAJUhDPYvYy38', 'My Ordinary Life-The Living Tombstone', '2017-10-23', 'The Living Tombstone'),
    (6, 'My Ordinary Life-The Living Tombstone', 'https://youtu.be/9Zj0JOHJR-s?si=MQyeAJUhDPYvYy38', 'My Ordinary Life-The Living Tombstone', '2017-10-23', 'The Living Tombstone')
]
try:
    cursor.executemany('INSERT INTO youtube_videos VALUES (?, ?, ?, ?, ?, ?)', videos)
except Exception as e:
    print(f'LUL {e}')



cursor.execute('UPDATE youtube_videos SET author = "OMFG" WHERE id = 4')
cursor.execute('DELETE FROM youtube_videos WHERE id = 6')

conn.commit()

cursor.execute('SELECT * FROM youtube_videos')
rows = cursor.fetchall()



print('Все строчки из таблицы: ', *rows)


