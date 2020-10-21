#import necessary libraries
import requests
import csv
from bs4 import BeautifulSoup

# Making request to url https://wwww.rithmschool.com/blog
response = requests.get("https://www.rithmschool.com/blog")

# Extract info from the file

# Creating BS parser
parser = BeautifulSoup(response.text, "html.parser")

#getting the articles as a list
articles = parser.findAll("article")
# Save into the CSV file the content of the blogpost

with open('Section 32 - Scraping with Beautiful Soup/scraping.csv', "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['title', 'url', 'date'])
#getting data necessary for each of the articles

    for article in articles:
        a_tag = article.find("a")
        #getting title
        title = a_tag.get_text() 
        #getting url 
        url = a_tag.attrs['href']
        #getting date
        date = article.find("time").attrs['datetime']
        csv_writer.writerow([title, url, date])
