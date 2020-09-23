#BAD
#traditional file read
# with open("fighters.csv") as file:
#   file.open()

from csv import reader, DictReader

#reader code
with open("Section 31 - Reading CSV\\fighters.csv") as file:
    csv_reader = reader(file) #returns iterator!! a list of rows that we can iterate over.
    next(csv_reader) #moves past the first line, so that we omit the header
    for fighter in csv_reader:
        #each row is a list
        print(f"{fighter[0]} is from {fighter[1]}")
    
#readers accept delimiter other than comma as kwargs, in case our data isn't delimited by commas (specify delimeter=" ")

#DictReader - ordered dict
with open("Section 31 - Reading CSV\\fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        #each row is an ordered dict! Uses first line for key values
        print(row['Name'] + " is from " + row['Country'])

