import sqlite3
CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class Parts:
    all = []
    def __init__(self, name, type, power, price, chipset = None, size = None, memory = None, total_memory = None, storage = None, pc = None):
        self._name = name
        self._type = type
        self._power = power
        self._price = price 
        self._chipset = chipset 
        self._size = size 
        self._memory = memory 
        self._total_memory = total_memory 
        self._storage = storage
        self._pc = pc
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name = property(get_name, set_name)
        
    def get_type(self):
        return self._type
    def set_type(self, type):
        self._type = type
    type = property(get_type, set_type)
        
    def get_power(self):
        return self._power
    def set_power(self, power):
        self._power = power
    power = property(get_power, set_power)
        
    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
    price = property(get_price, set_price)
        
    def get_chipset(self):
        return self._chipset
    def set_chipset(self, chipset):
        self._chipset = chipset
    chipset = property(get_chipset, set_chipset)
        
    def get_size(self):
        return self._size
    def set_size(self, size):
        self._size = size
    size = property(get_size, set_size)
        
    def get_memory(self):
        return self._memory
    def set_memory(self, memory):
        self._memory = memory
    memory = property(get_memory, set_memory)
            
    def get_total_memory(self):
        return self._total_memory
    def set_total_memory(self, total_memory):
        self._total_memory = total_memory
    total_memory = property(get_total_memory, set_total_memory)
            
    def get_storage(self):
        return self._storage
    def set_storage(self, storage):
        self._storage = storage
    storage = property(get_storage, set_storage)

    def get_pc(self):
        return self._pc
    def set_pc(self, pc):
        self._pc = pc
    pc = property(get_pc, set_pc)

    @classmethod
    def create_table(cls):
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS parts(
                id INTEGER PRIMARY KEY,
                name TEXT,
                type TEXT,
                power INTEGER,
                price INTEGER,
                chipset TEXT,
                size TEXT,
                memory TEXT,
                total_memory INTEGER,
                storage INTEGER,
                pc INTEGER
            )
        '''
        CURSOR.execute(create_table_sql)

    @classmethod
    def drop_table(cls):
        drop_table_sql = "DROP TABLE IF EXISTS parts"
        CURSOR.execute(drop_table_sql)

    def save(self):
        save_sql = '''
            INSERT INTO parts(name, type, power, price, chipset, size, memory, total_memory, storage, pc)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        parameter = (self.name, self.type, self.power, self.price, self.chipset, self.size, self.memory, self.total_memory, self.storage, self.pc)
        CURSOR.execute(save_sql, parameter)
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def add_parts(cls, name, type, power, price, chipset, size, memory, total_memory, storage, pc):
        new_part = Parts(name, type, power, price, chipset, size, memory, total_memory, storage, pc)
        new_part.save()

    @classmethod
    def delete_all(cls):
        delete_sql = '''
            DELETE FROM parts
        '''
        CURSOR.execute(delete_sql)
        CONN.commit()

    @classmethod
    def delete_children_pc(cls, pc):
        sql = '''
            DELETE FROM parts WHERE pc = ?
        '''
        parameter = (pc,)
        CURSOR.execute(sql, parameter)
        CONN.commit()