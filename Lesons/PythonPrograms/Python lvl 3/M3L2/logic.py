import sqlite3
from config import DATABASE

class DB_Manager:


    def __init__(self, database):
        self.database = database # имя базы данных
        

    
    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
            conn.execute('''
                CREATE TABLE projects (
                        project_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        project_name TEXT,
                        description TEXT,
                        url TEXT,
                        status_id INTEGER,
                        FOREIGN KEY(status_id) REFERENCES status(status_id) 
                )
            ''')     
        # дз: создать другие таблицы    
            conn.execute('''
                CREATE TABLE status (
                        status_id INTGER PRIMARY KEY, 
                        Status_name TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE projects_skills (
                        skill_id INTGER PRIMARY KEY, 
                        project_id INTEGER,
                        FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                )
            ''')          
            conn.execute('''
                CREATE TABLE skills (
                        skill_id INTGER PRIMARY KEY, 
                        skill_name TEXT
                )
            ''')
            conn.commit()
        pass   
        print('База данных создана')

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()        