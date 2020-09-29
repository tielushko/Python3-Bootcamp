'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

import csv

def add_user(first_name, last_name):
    with open('users.csv', 'a') as file:
        csv_row = [first_name, last_name]
        csv_writer = csv.writer(file)
        csv_writer.writerow(csv_row)


'''
print_users() # None
# prints to the console:
# Colt Steele
'''

def print_users():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row["First Name"] + " " + row["Last Name"])

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

def find_user(first_name, last_name):
    pass

''' Version  1
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        index = 0
        for row in csv_reader:
            index += 1
            if first_name == row["First Name"] and last_name == row["Last Name"]:
                return index
        return "{} {} not found.".format(first_name, last_name)



''' Version  2
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)


''' Version 1
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
import csv

def update_users(old_first, old_last, new_first, new_last):
    index = 0
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["First Name"] == old_first and row["Last Name"] == old_last:
                row["First Name"] = new_first
                row["Last Name"] = new_last
                index += 1
        people = list(csv_reader)
        
    with open("users.csv", "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=csv_reader.fieldnames)
        csv_writer.writeheader()
        for person in people:
            csv_writer.writerow({
                "First Name": person["First Name"],
                "Last Name": person["Last Name"]
            })
    return "Users updated: {}.".format(index)

"""Version 2
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
"""

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    count = 0
    
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
    
    return "Users updated: {}.".format(count)


'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

def delete_users(first, last):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
    
    count = 0

    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                csv_writer.writerow(row)
    return "Users deleted: {}.".format(count)
