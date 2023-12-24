import tkinter as tk
from tkinter import messagebox
import sqlite3

class RecipeOrganizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Organizer")
        self.master.geometry("600x400")

        self.db_connection = sqlite3.connect("recipes_database.db")
        self.create_table()

        self.label_title = tk.Label(self.master, text="Recipe Title:")
        self.label_title.pack()

        self.entry_title = tk.Entry(self.master)
        self.entry_title.pack()

        self.label_ingredients = tk.Label(self.master, text="Ingredients:")
        self.label_ingredients.pack()

        self.text_ingredients = tk.Text(self.master, height=5, width=40)
        self.text_ingredients.pack()

        self.label_instructions = tk.Label(self.master, text="Instructions:")
        self.label_instructions.pack()

        self.text_instructions = tk.Text(self.master, height=5, width=40)
        self.text_instructions.pack()

        self.label_category = tk.Label(self.master, text="Category:")
        self.label_category.pack()

        self.entry_category = tk.Entry(self.master)
        self.entry_category.pack()

        self.button_add_recipe = tk.Button(self.master, text="Add Recipe", command=self.add_recipe)
        self.button_add_recipe.pack(pady=10)

        self.recipe_listbox = tk.Listbox(self.master)
        self.recipe_listbox.pack(expand=True, fill="both")

        self.load_recipes()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS recipes 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           title TEXT, 
                           ingredients TEXT, 
                           instructions TEXT, 
                           category TEXT)''')
        self.db_connection.commit()

    def add_recipe(self):
        title = self.entry_title.get()
        ingredients = self.text_ingredients.get("1.0", tk.END).strip()
        instructions = self.text_instructions.get("1.0", tk.END).strip()
        category = self.entry_category.get()

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO recipes (title, ingredients, instructions, category) VALUES (?, ?, ?, ?)",
                       (title, ingredients, instructions, category))
        self.db_connection.commit()

        self.load_recipes()

    def load_recipes(self):
        self.recipe_listbox.delete(0, tk.END)

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id, title, category FROM recipes")

        for row in cursor.fetchall():
            recipe_str = f"{row[1]} - {row[2]}"
            self.recipe_listbox.insert(tk.END, recipe_str)

if __name__ == "__main__":
    root = tk.Tk()
    recipe_organizer_app = RecipeOrganizerApp(root)
    root.mainloop()
