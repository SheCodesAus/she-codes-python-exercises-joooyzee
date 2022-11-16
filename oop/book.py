'''
Databases = used to structure and store large amounts of information/data
SQL = structured query language; used to retrieve data in a specified way from databases

You don't need to know the details of how the code works below. 
This is just an exercise to demonstrate that using databases and SQL this way is finicky, 
to give you an appreciation for why tools like Django exist.
'''
import sqlite3

# creates a database named books.db and connects to it
connection = sqlite3.connect("books.db")

# cursor is an object that allows us to interact with the databse
cursor = connection.cursor()

## create a table called 'book' and fields 'id', 'title', 'pages', 'current_page'
# cursor.execute("""
#     CREATE TABLE book (
#         id integer PRIMARY KEY,
#         title TEXT,
#         pages INTEGER,
#         current_page INTEGER
#     )
# """
# )

## add a record
# cursor.execute("""
#     INSERT INTO book VALUES (
#         0, 'A great book', 213, 27
#     )
# """)

## add another record
# cursor.execute("""
#     INSERT INTO book VALUES (
#         1, 'Another great book', 233, 42
#     )
# """)

## commit our changes
# connection.commit()

# retrieve records
rows = cursor.execute("SELECT title, pages, current_page FROM book")
for row in rows:
    print(row)

connection.close()

"""
Note: we passed SQL as a string e.g. ("SELECT title, pages, current_page FROM book")
This is super finicky - and makes it difficult to debug when things go wrong
(e.g. no syntax highlighting, or error messages pointing out which line in our code had issues)

With the use of tools like Django, we'd be able to retrieve records in a similar way to:
book_list = BookTable.query(author="JK Rowling")

Note: BookTable -> class
.query() -> method
"""