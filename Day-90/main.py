#News App in Python
import requests
import json

API_KEY = '938ebe8e8808415e845ae2ffe0d47823'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def get_news(category):
    params = {
        'apiKey': API_KEY,
        'category': category,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        articles = data.get('articles', [])

        if articles:
            print(f"--- {category.capitalize()} News ---")
            for index, article in enumerate(articles, start=1):
                print(f"{index}. {article['title']}")
                print(article['url'])
                print()
        else:
            print(f"No {category} news available.")
    else:
        print(f"Failed to fetch {category} news. Error: {response.status_code}")

if __name__ == '__main__':
    while True:
        category = input("Enter the category of news you want to see (e.g., sports, technology, business): ")
        
        if category.lower() == 'exit':
            break

        if category.lower() not in ['business', 'technology', 'entertainment', 'health', 'science', 'sports', 'gaming']:
            print("Invalid category. Please choose from the available categories.")
            continue

        get_news(category)