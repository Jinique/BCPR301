import sqlite3


class DbWriter:

    def __init__(self):
        self.my_db = 'interpreter.db'

    def start_db(self):
        try:
            my_conn = sqlite3.connect(self.my_db)
        except Exception as e:
            print(e)
        finally:
            print("Connection complete")
            print(f"Opened {self.my_db} successfully")
            return my_conn

    def write_db(self, new_module):
        my_conn = self.start_db()
        print("my conn done")
        c = my_conn.cursor()
        print("cursor set")
        # try:
        # drop existing tables
        c.execute("""DROP TABLE IF EXISTS class;""")
        c.execute("""DROP TABLE IF EXISTS attribute;""")
        c.execute("""DROP TABLE IF EXISTS method;""")
        c.execute("""DROP TABLE IF EXISTS method_att;""")
        print("all table dropped")
        c.execute('''
                    CREATE TABLE class (
                    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    class_name VARCHAR(30));
                    ''')
        print("make class")
        c.execute('''
                    CREATE TABLE attribute (
                    attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    attribute_name VARCHAR(30),
                    attribute_type VARCHAR(10),
                    class_id INTEGER,
                    FOREIGN KEY (class_id) REFERENCES class(class_id));
                    ''')
        print("make att")
        c.execute('''
                    CREATE TABLE method (
                    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    method_name VARCHAR(30),
                    method_input VARCHAR(20),
                    method_type VARCHAR(10),
                    class_id INTEGER,
                    FOREIGN KEY (class_id) REFERENCES class(class_id));
                    ''')
        print("make method")
        c.execute('''
                    CREATE TABLE method_att (
                    method_att_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    method_att_name VARCHAR(30),
                    method_att_type VARCHAR(10),
                    method_id INTEGER,
                    FOREIGN KEY (method_id) REFERENCES method(method_id));
                    ''')
        print("make method_att")

        my_conn.commit()

    def read_db(self):
        my_conn = self.start_db()
        c = my_conn.cursor()
        # only for demo
        class_data = ["ClassBuilder", "Attribute", "Method", "Relationship"]
        for a_data in class_data:
            format_str = """INSERT INTO class (class_id, class_name) 
            VALUES (NULL, "{first}");"""
            sql_command = format_str.format(first=a_data)
            c.execute(sql_command)
        c.execute("SELECT * FROM class")
        result = c.fetchall()
        print(result)
        """
        for row in c.execute('SELECT * FROM class'):
            print(row)
        """
        # create database close()
