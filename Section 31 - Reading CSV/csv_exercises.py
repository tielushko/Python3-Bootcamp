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