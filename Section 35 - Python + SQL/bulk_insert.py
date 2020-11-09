import sqlite3

connector = sqlite3.connect("my_friends.db")

cursor = connector.cursor()
cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)
]

# pass in query, then people using executemany
cursor.executemany("INSERT INTO friends VALUES(?,?,?)", people)

# the method with for loop - if we need to do something else at each steps
for person in people:
    cursor.execute("INSERT INTO friends VALUES(?,?,?)", person)

connector.commit()
connector.close()