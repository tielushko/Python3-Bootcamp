from csv import reader, writer

with open("Section 31 - Reading CSV\\fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[item.upper() for item in row]for row in csv_reader]

with open("Section 31 - Reading CSV\\screaming_fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerows(fighters)