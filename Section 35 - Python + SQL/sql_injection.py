import sqlite3

conn = sqlite3.connect('users.db')
username = input('Please enter the username...\n')
password = input('Please enter your password...\n')

# BAD BAD BAD WAY as the user can write sql to inject into it
# query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

# how it basically does it is it selects adds ' OR 1=1 -- => 'ends the password in empty string, then or 1=1 by default will return correct password and comment will remove the rest

# GOOD GOOD GOOD WAY TO DO IT!
query = "SELECT * FROM users WHERE username=? AND password=?"
c = conn.cursor()
c.execute(query, (username, password)) # prevents us to add other sql code from command line

result = c.fetchone()

if result:
    print('Welcome Back')
else: 
    print("FAILED LOGIN")

conn.commit()
conn.close()