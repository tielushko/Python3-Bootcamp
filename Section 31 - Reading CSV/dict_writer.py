"""
DictWriter - creates a writer object for writing using dictionaries
fieldnames - kwarg for the DictWriter to specify headers
writeheader - method on the writer to write header row 
writerow - write a row based on the dictionary
"""

from csv import DictWriter

with open("Section 31 - Reading CSV\\cats.csv", "w") as file:
    header = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=header)
    csv_writer.writeheader()
    csv_writer.writerow({ #order doesn't matter btw unlike in list.
        "Name": "Blue",
        "Breed": "Garfield",
        "Age": 10
    })

