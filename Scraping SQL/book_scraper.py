import sqlite3
from bs4 import BeautifulSoup
import requests

# variables used globally in the program

# url to scrape from 
url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"

# database file name
database_file = "books.db"

# dictionary that is used to map the word class name to the integer of the rating.
rating_matching_dict = { 
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

def scrape_book_save_to_db(url):
    request = requests.get(url) # get the request from the url
    parser = BeautifulSoup(request.text, "html.parser") # capture the html of the request and parse it using BeautifulSoup
    all_books_data = []  #create empty list to store all the books
    books = parser.findAll(class_="product_pod")  # get the list of all the books found on the webpage
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book)) # store the book data from the page in a tuple
        all_books_data.append(book_data)
    save_to_db(all_books_data)

def save_to_db(all_books_data): 
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books (TITLE TEXT, PRICE REAL, RATING INTEGER)")
    cursor.executemany("INSERT INTO books VALUES(?,?,?)", all_books_data)

    connection.commit()
    connection.close()

def get_title(book):
    title = book.find('h3').find('a')['title']     # capture the h3 of the title, find the a tag within h3, and scan the title attribute of a tag
    return title    # return our title

def get_price(book):
    price = float(book.find(class_="price_color").get_text()[2:]) #find the price_color class that responsible for the price -> get_text to remove the markup, then slice it starting from 2nd index to remove the first 2 faulty characters, then convert and store as a float.
    return price

def get_rating(book):
    rating_text = book.find(class_="star-rating").get_attribute_list('class')[-1]   # find the star-rating list of each of the book, then the element at last index is our actual rating but it represented as text example("One", "Two", etc.)
    rating_int = rating_matching_dict[rating_text]  # mapping of the class textual representation of the book rating to the integer value
    return rating_int   #return integer rating of the book

# main method sort of where we call out our scrape and save to db
scrape_book_save_to_db(url)