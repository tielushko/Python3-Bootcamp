import sqlite3

# create a connector to the friends database - can link existing or create a new one
connector = sqlite3.connect('my_friends.db') 

#cursor concept creates a way for our sql commands to be implemented. we execute sql lines on that cursor

# making cursor object
cursor = connector.cursor()

# executing some changes 

# creating the table
# cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# inserting data into the tables
# insert_query = """INSERT INTO friends VALUES ('Mary', 'Lewis', 7)"""

# BAD WAY
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY!!!!
form_first = "Mary-Todd"
query = f"INSERT INTO friends (first_name) VALUES (?)"
cursor.execute(query, (form_first,))


# BETTER WAY WITH VARIOUS DATA MATCHING COLUMNS
data = ("Steve", "irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
cursor.execute(query, data)

# commit changes to the database to the connector
connector.commit()
# must close connection to the file of the database
connector.close()