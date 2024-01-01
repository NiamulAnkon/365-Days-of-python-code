import tkinter as tk
import requests

class QuoteOfTheDayApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quote of the Day")
        self.master.geometry("600x300")

        self.quote_label = tk.Label(self.master, text="")
        self.quote_label.pack(pady=20)

        self.fetch_button = tk.Button(self.master, text="Fetch Quote of the Day", command=self.fetch_quote)
        self.fetch_button.pack(pady=10)

    def fetch_quote(self):
        api_url = "https://quotes.rest/qod"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            quote = data["contents"]["quotes"][0]["quote"]
            author = data["contents"]["quotes"][0]["author"]

            full_quote = f'"{quote}" - {author}'
            self.quote_label.config(text=full_quote)
        else:
            self.quote_label.config(text="Failed to fetch the quote.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteOfTheDayApp(root)
    root.mainloop()
