import tkinter as tk
from tkinter import messagebox
import sqlite3
from cryptography.fernet import Fernet
from datetime import datetime

class JournalApp:
    def __init__(self, master_root):
        self.master = master_root
        self.master.title("Daily Journal App")
        self.master.geometry("600x400")

        self.db_connection = sqlite3.connect("user_journals_database.db")
        self.create_table()

        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        self.label_title = tk.Label(self.master, text="Daily Journal App", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=10)

        self.text_entry = tk.Text(self.master, height=10, width=50)
        self.text_entry.pack(pady=10)

        self.button_save = tk.Button(self.master, text="Save Entry", command=self.save_entry)
        self.button_save.pack(pady=5)

        self.button_view_entries = tk.Button(self.master, text="View Entries", command=self.view_entries)
        self.button_view_entries.pack(pady=5)

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS journal_entries 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           date TEXT, 
                           entry TEXT)''')
        self.db_connection.commit()

    def save_entry(self):
        entry_text = self.text_entry.get("1.0", "end-1c").strip()
        if not entry_text:
            messagebox.showwarning("Empty Entry", "Please write something")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        encrypted_entry = self.encrypt_entry(entry_text)

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO journal_entries (date, entry) VALUES (?, ?)", (timestamp, encrypted_entry))
        self.db_connection.commit()

        messagebox.showinfo("Entry Saved", "Your journal entry has been saved correctly.")
        self.text_entry.delete("1.0", "end")

    def view_entries(self):
        entries_window = tk.Toplevel(self.master)
        entries_window.title("Journal Entries")

        scrollbar = tk.Scrollbar(entries_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(entries_window, yscrollcommand=scrollbar.set, width=70, height=20)
        listbox.pack(pady=10)

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT date, entry FROM journal_entries ORDER BY date DESC")

        for row in cursor.fetchall():
            date = row[0]
            decrypted_entry = self.decrypt_entry(row[1])
            listbox.insert(tk.END, f"{date}\n{decrypted_entry}\n{'-' * 50}")

        scrollbar.config(command=listbox.yview)

    def encrypt_entry(self, entry):
        encrypted_entry = self.cipher_suite.encrypt(entry.encode())
        return encrypted_entry.decode()

    def decrypt_entry(self, encrypted_entry):
        decrypted_entry = self.cipher_suite.decrypt(encrypted_entry.encode())
        return decrypted_entry.decode()


if __name__ == "__main__":
    root = tk.Tk()
    daily_journal_app = JournalApp(root)
    root.mainloop()
