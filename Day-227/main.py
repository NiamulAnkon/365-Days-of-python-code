import tkinter as tk
from tkinter import ttk
from tkinter import *
import time

class VirtualMuseum:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Museum Tour Guide")
        self.root.geometry("500x500")

        self.artworks = {
            "Monalisa": "Leonardo da Vinci, Oil on canvas, 1503–1506",
            "Starry Night": "Vincent van Gogh, Oil on canvas, 1889",
            "The Persistence of Memory": "Salvador Dalí, Oil on canvas, 1931",
        }
        self.rooms = {
            "Room 1": ["Monalisa", "Starry Night"],
            "Room 2": ["The Persistence of Memory"],
        }

        self.room_label = ttk.Label(root, text="Rooms Available:")
        self.room_label.pack()

        self.room_combobox = ttk.Combobox(root, values=list(self.rooms.keys()))
        self.room_combobox.pack()

        self.explore_button = ttk.Button(root, text="Explore", command=self.explore_room)
        self.explore_button.pack()

        self.artwork_label = ttk.Label(root, text="")
        self.artwork_label.pack()

    def explore_room(self):
        room_name = self.room_combobox.get()
        if room_name in self.rooms:
            artworks_in_room = self.rooms[room_name]
            for artwork in artworks_in_room:
                self.display_artwork(artwork)
                time.sleep(2)
        else:
            self.artwork_label.config(text="Room not found.")

    def display_artwork(self, artwork_name):
        if artwork_name in self.artworks:
            artwork_info = f"Artwork: {artwork_name}\nDetails: {self.artworks[artwork_name]}"
            self.artwork_label.config(text=artwork_info)
        else:
            self.artwork_label.config(text="Artwork not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualMuseum(root)
    root.mainloop()
