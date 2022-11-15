'''
Databases = used to structure and store large amounts of information/data
SQL = structured query language; used to retrieve data in a specified way from databases
'''
import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE book (
#         id integer PRIMARY KEY,
#         title TEXT,
#         pages INTEGER,
#         current_page INTEGER
#     )
# """
# )

# cursor.execute("""
#     INSERT INTO book VALUES (
#         0, 'A great book', 213, 27
#     )
# """)

# cursor.execute("""
#     INSERT INTO book VALUES (
#         1, 'Another great book', 233, 42
#     )
# """)

# connection.commit()

rows = cursor.execute("SELECT title, pages, current_page FROM book")
for row in rows:
    print(row)

connection.close()