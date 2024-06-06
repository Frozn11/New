import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('marvel.db')
cursor = conn.cursor()

# Название таблицы
table_name = 'marvel'

# Название нового столбца и его тип данных
new_column_name = 'enemy'
new_column_type = 'TEXT'

# Выполнение запроса на добавление столбца
conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (

          )''') 
alter_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_type}"
cursor.execute(alter_query)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

