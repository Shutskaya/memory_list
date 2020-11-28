import sqlite3


class SqliteDB:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_list(self, name):
        query_add_list = "INSERT INTO list (name) values (?)"
        data = (name,)
        self.cursor.execute(query_add_list, data)
        self.conn.commit()

    def add_records(self, list_id, value):
        query_add_records = "INSERT INTO records (list_id, value) VALUES (?, ?)"
        data = (list_id, value)
        self.cursor.execute(query_add_records, data)
        self.conn.commit()

    def delete_list(self, list_id):
        query_delete_list = "DELETE FROM list WHERE id = ?"
        data = (list_id,)
        self.set_pragma()
        self.cursor.execute(query_delete_list, data)
        self.conn.commit()

    def delete_records(self, records_id):
        query_delete_records = "DELETE FROM records WHERE id = ?"
        data = (records_id, )
        self.cursor.execute(query_delete_records, data)
        self.conn.commit()

    def set_pragma(self):
        self.cursor.execute("PRAGMA FOREIGN_KEYS=on;")


def create_struct():
    query_create_table_list = "CREATE TABLE IF NOT EXISTS list (" \
                              "id integer PRIMARY KEY," \
                              "name text NOT NULL);"
    query_crate_table_records = "CREATE TABLE IF NOT EXISTS records(" \
                                "id integer PRIMARY KEY," \
                                "list_id integer NOT NULL," \
                                "value text NOT NULL," \
                                "FOREIGN KEY(list_id) REFERENCES list(id))"
    enable_suport_foreignkey = "PRAGMA foreign_keys = on"
    db = SqliteDB()
    db.execute_query(query_create_table_list)
    db.execute_query(query_crate_table_records)
    db.execute_query(enable_suport_foreignkey)
    db.close()


if __name__ == '__main__':
    db = SqliteDB()
    db.delete_records(15)
    db.close()
