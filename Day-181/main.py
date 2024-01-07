import tkinter as tk
from tkinter import messagebox

class NoteTakerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Note Taker")
        self.master.geometry("400x400")

        self.notes_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.notes_listbox.pack(pady=10)

        self.load_notes()

        self.note_entry = tk.Entry(self.master, width=30)
        self.note_entry.pack(pady=5)

        self.add_button = tk.Button(self.master, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.master, text="View Note", command=self.view_note)
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Note", command=self.delete_note)
        self.delete_button.pack(pady=5)

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                for note in notes:
                    self.notes_listbox.insert(tk.END, note.strip())
        except FileNotFoundError:
            pass

    def add_note(self):
        new_note = self.note_entry.get()
        if new_note:
            self.notes_listbox.insert(tk.END, new_note)
            self.save_notes()
            self.note_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Note", "Please enter a note.")

    def view_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            selected_note = self.notes_listbox.get(selected_index)
            messagebox.showinfo("Note", selected_note)
        else:
            messagebox.showwarning("No Selection", "Please select a note to view.")

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            self.notes_listbox.delete(selected_index)
            self.save_notes()
        else:
            messagebox.showwarning("No Selection", "Please select a note to delete.")

    def save_notes(self):
        with open("notes.txt", "w") as file:
            notes = [self.notes_listbox.get(i) + "\n" for i in range(self.notes_listbox.size())]
            file.writelines(notes)

if __name__ == "__main__":
    root = tk.Tk()
    app_note_taker = NoteTakerApp(root)
    root.mainloop()
