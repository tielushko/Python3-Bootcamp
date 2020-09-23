from csv import DictReader, DictWriter

def cm_to_inches(cm):
    return float(cm) / 2.54

with open("Section 31 - Reading CSV\\fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("Section 31 - Reading CSV\\fighters_in_inches.csv", "w") as file:
    headers = ("Name","Country","Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for fighter in fighters:
        csv_writer.writerow({
            "Name": fighter["Name"],
            "Country" : fighter["Country"],
            "Height": cm_to_inches(fighter["Height (in cm)"])
        })