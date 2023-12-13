import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime

class personaldiaryapp:
    def __init__(self, root_master):
        self.root_master = root_master
        self.root_master.title("Personal Diary App")
        self.root_master.geometry("700x500")

        self.text_entry = tk.Text(self.root_master, height=10, width=40)
        self.text_entry.pack(pady=10)

        save_button = tk.Button(self.root_master, text="Save Entry", command=self.save_entry)
        save_button.pack(pady=5)

        self.load_button = tk.Button(self.root_master, text="Load Entry", command=self.load_entry)
        self.load_button.pack(pady=5)

    def save_entry(self):
        entry_text = self.text_entry.get("1.0", "end-1c")
        if not entry_text.strip():
            messagebox.showwarning("Empty Entry", "Please write something")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Diary_{timestamp}.txt"

        with open(filename, "w") as file:
            file.write(entry_text)

        messagebox.showinfo("Entry Saved", "Your Diary has been saved.")
        self.text_entry.delete("1.0", "end")

    def load_entry(self):
        entry_file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if entry_file:
            with open(entry_file, "r") as file:
                entry_text = file.read()

                self.text_entry.delete("1.0", "end")
                self.text_entry.insert("1.0", entry_text)

if __name__== "__main__":
    root = tk.Tk()
    software_app = personaldiaryapp(root)
    root.mainloop()
