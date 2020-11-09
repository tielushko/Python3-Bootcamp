import sqlite3

connector = sqlite3.connect("my_friends.db")

cursor = connector.cursor()

# cursor.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")

cursor.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

# cursor is an iterable object
# gets the values in the table -> returns as a tuple
# for result in cursor:
#     print(result) 

# fetch all method that returns these tupled rows as a list
# print(cursor.fetchone())
print(cursor.fetchall())

connector.commit()
connector.close()