import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('article', class_='product_pod')

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Rating'])

    for product in products:
        name = product.h3.a['title']
        price = product.find('p', class_='price_color').text
        rating_class = product.p['class'][1]  # e.g. 'One', 'Two', etc.

        # Convert rating text to number
        ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = ratings.get(rating_class, 0)

        writer.writerow([name, price, rating])

print("Data saved to products.csv")
