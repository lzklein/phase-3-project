import sqlite3
CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class Pc:
    all = []
    def __init__(self, name, user, id = None):
        self._name = name
        self._user = user
        self.id = id
        self.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    def get_user(self):
        return self._user
    def set_user(self, user):
        self._user = user
    user = property(get_user, set_user)

    @classmethod
    def create_table(cls):
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS pcs(
                id INTEGER PRIMARY KEY,
                name TEXT,
                user TEXT
            )
        '''
        CURSOR.execute(create_table_sql)

    @classmethod
    def drop_table(cls):
        drop_table_sql = "DROP TABLE IF EXISTS pcs"
        CURSOR.execute(drop_table_sql)

    def save(self):
        save_sql = '''
            INSERT INTO pcs (name, user)
            VALUES (?, ?)
        '''
        parameter = (self.name, self.user)
        CURSOR.execute(save_sql, parameter)
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def add_Pc(cls, name, user):
        new_pc = Pc(name, user)
        new_pc.save()

    @classmethod
    def delete_all(cls):
        delete_sql = '''
            DELETE FROM pcs
        '''
        CURSOR.execute(delete_sql)
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM pcs"
        response = CURSOR.execute(sql)
        all_pcs = response.fetchall()
        return all_pcs
    
    @classmethod
    def delete_one(cls, name):
        sql = '''
            DELETE FROM pcs WHERE name = ?
        '''
        parameter = (name,)
        CURSOR.execute(sql, parameter)
        CONN.commit()