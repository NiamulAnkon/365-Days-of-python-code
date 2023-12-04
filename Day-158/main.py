import pyjokes
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Jokes Generator")
root.geometry("500x300")

def generate_jokes():
    jokes_folder = open("jokes.txt", 'w')

    for i in range(1, 51):
        jokes_folder.write(str(i) + ' ')
        jokes_folder.write(pyjokes.get_joke())
        jokes_folder.write('\n\n')

    jokes_folder.close()
    message_label.config(text="Jokes generated and saved to jokes.txt!")

joke_button = ttk.Button(root, text="Generate Jokes", command=generate_jokes)
joke_button.pack(pady=10)

message_label = ttk.Label(root, text="")
message_label.pack(pady=10)

root.mainloop()
