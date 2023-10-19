import string
import random

url_db = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(long_url):
    if long_url in url_db:
        return url_db[long_url]
    else:
        short_url = generate_short_url()
        url_db[long_url] = short_url
        return short_url

def access_url(short_url):
    for long_url, url_key in url_db.items():
        if url_key == short_url:
            return long_url
    return "Short URL not found."

if __name__ == "__main__":
    while True:
        print("Options: \n1. Shorten URL \n2. Access URL \n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            long_url = input("Enter the long URL: ")
            short_url = shorten_url(long_url)
            print(f"Shortened URL: http://short.ly/{short_url}")
        elif choice == "2":
            short_url = input("Enter the short URL: ")
            long_url = access_url(short_url)
            if long_url != "Short URL not found.":
                print(f"Original URL: {long_url}")
            else:
                print(long_url)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
