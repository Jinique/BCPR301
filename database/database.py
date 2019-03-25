import sqlite3
from module_builder.class_builder import ClassBuilder

try:
    conn = sqlite3.connect("interpreter.db")
except Exception as e:
    print(e)
else:
    print("Opened database successfully")
finally:
    print("Finishing connecting to database")

cur = conn.cursor()

# delete
cur.execute("""DROP TABLE class;""")
cur.execute("""DROP TABLE attribute;""")
cur.execute("""DROP TABLE method;""")
cur.execute("""DROP TABLE method_att;""")

sql_command = """
CREATE TABLE class (
class_id INTEGER PRIMARY KEY AUTOINCREMENT,
class_name VARCHAR(30));"""

cur.execute(sql_command)

sql_command = """
CREATE TABLE attribute (
attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
attribute_name VARCHAR(30),
attribute_type VARCHAR(10),
class_id INTEGER,
FOREIGN KEY (class_id) REFERENCES class(class_id));
"""
cur.execute(sql_command)

sql_command = """
CREATE TABLE method (
method_id INTEGER PRIMARY KEY AUTOINCREMENT,
method_name VARCHAR(30),
method_type VARCHAR(10),
class_id INTEGER,
FOREIGN KEY (class_id) REFERENCES class(class_id));
"""
cur.execute(sql_command)

sql_command = """
CREATE TABLE method_att (
method_att_id INTEGER PRIMARY KEY AUTOINCREMENT,
method_att_name VARCHAR(30),
method_att_type VARCHAR(10),
method_id INTEGER,
FOREIGN KEY (method_id) REFERENCES method(method_id));
"""
cur.execute(sql_command)

# sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
#     VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
# cursor.execute(sql_command)
#
# sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
#     VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
# cursor.execute(sql_command)

# staff_data = [("William", "Shakespeare", "m", "1961-10-25"),
#               ("Frank", "Schiller", "m", "1955-08-17")]

# for p in staff_data:
#   format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
#   VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""
#
#   sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate = p[3])
#   cur.execute(sql_command)

class_data = ["ClassBuilder", "Attribute", "Method", "Relationship"]
# class_data = [("1", "one"), ("2", "two"), ("3", "three")]

for a_data in class_data:
    format_str = """INSERT INTO class (class_id, class_name) 
    VALUES (NULL, "{first}");"""
    sql_command = format_str.format(first=a_data)
    cur.execute(sql_command)

conn.commit()


cur.execute("SELECT * FROM class")
print("fetchall:")
result = cur.fetchall()
for r in result:
    print(r)
cur.execute("SELECT * FROM class")
print("\nfetch one:")
res = cur.fetchone()
print(res)


conn.close()

print(class_data)