import sqlite3

class Repository:
    _create_table_statement = 'CREATE TABLE IF NOT EXISTS {table_name} ({params})'
    _add_item_statement = 'INSERT INTO {table_name} VALUES ({values})'
    _delete_item_statement = 'DELETE FROM {table_name} WHERE {condition}'
    _get_all_items_statement = 'SELECT {values} FROM {table_name} WHERE {condition}'

    def __init__(self, dbname):
        if not dbname:
            raise ValueError(dbname)

        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
    
    def setup(self):
        pass