import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

data_element = soup.find("div", class_="product-info")

product_name = data_element.find("h1").text
product_price = data_element.find("span", class_="price").text

print("Product name:", product_name)
print("Product price:", product_price)