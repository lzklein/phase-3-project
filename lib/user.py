import sqlite3
CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class User:
    all = []
    def __init__(self, name, id=None):
        self._name = name
        self.id = id
        self.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    @classmethod
    def create_table(cls):
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        '''
        CURSOR.execute(create_table_sql)

    @classmethod
    def drop_table(cls):
        drop_table_sql = "DROP TABLE IF EXISTS users"
        CURSOR.execute(drop_table_sql)

    def save(self):
        save_sql = '''
            INSERT INTO users (name)
            VALUES (?)
        '''
        parameter = (self.name,)
        CURSOR.execute(save_sql, parameter)
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def add_name(cls, name):
        new_name = User(name)
        new_name.save()

    @classmethod
    def delete_all(cls):
        delete_sql = '''
            DELETE FROM users
        '''
        CURSOR.execute(delete_sql)
        CONN.commit()