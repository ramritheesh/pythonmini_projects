import requests, csv
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

response = requests.get(URL)

print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")
all_books = soup.find_all("article", class_ = "product_pod")
books_data = []

for book in all_books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    book_info = {
        "title": title,
        "price": price,
        "rating": f"{rating} stars"
    }
    books_data.append(book_info)
    
with open("book.csv", "w", newline="", encoding="utf-8") as file:
    headers = ["title", "price", "rating"]
    writer = csv.DictWriter(file, fieldnames= headers)
    writer.writeheader()
    writer.writerows(books_data)

print("Scrapping Complete!, check for book.csv it will be there")
    