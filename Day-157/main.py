import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk
import wikipedia
from wordcloud import WordCloud, STOPWORDS

class WordCloudGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Cloud Generator")
        self.master.geometry("400x200")

        self.label = ttk.Label(master, text="Enter the name you want to make a word cloud:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack(pady=10)

        self.generate_button = ttk.Button(master, text="Generate Word Cloud", command=self.generate_wordcloud)
        self.generate_button.pack(pady=10)

    def generate_wordcloud(self):
        query = self.entry.get()
        if query:
            title = wikipedia.search(query)[0]
            page = wikipedia.page(title)
            text = page.content

            bg_path = filedialog.askopenfilename(title="Select Background Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if bg_path:
                bg = np.array(Image.open(bg_path))
                unwanted_words = set(STOPWORDS)

                wordcloud = WordCloud(background_color="red", max_words=400, mask=bg, stopwords=unwanted_words)
                wordcloud.generate(text)

                save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
                if save_path:
                    wordcloud.to_file(save_path)
                    tk.messagebox.showinfo("Word Cloud Generated", "Word cloud saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCloudGenerator(root)
    root.mainloop()
