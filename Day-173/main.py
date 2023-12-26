import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import face_recognition
from PIL import Image, ImageTk

class FaceRecognitionLoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition Login")
        self.master.geometry("400x400")

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()

        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.master, textvariable=self.name_var)
        self.entry_name.pack()

        self.label_age = tk.Label(self.master, text="Age:")
        self.label_age.pack()

        self.entry_age = tk.Entry(self.master, textvariable=self.age_var)
        self.entry_age.pack()

        self.label_gender = tk.Label(self.master, text="Gender:")
        self.label_gender.pack()

        self.entry_gender = tk.Entry(self.master, textvariable=self.gender_var)
        self.entry_gender.pack()

        self.button_browse = tk.Button(self.master, text="Browse Image", command=self.browse_image)
        self.button_browse.pack()

        self.button_login = tk.Button(self.master, text="Login", command=self.login)
        self.button_login.pack()

        self.label_result = tk.Label(self.master, text="")
        self.label_result.pack()

        self.face_image_label = tk.Label(self.master)
        self.face_image_label.pack()

        self.known_face_encoding = None

    def browse_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.known_face_encoding = self.encode_face(file_path)
            self.display_face_image(file_path)

    def encode_face(self, file_path):
        image = face_recognition.load_image_file(file_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding

    def display_face_image(self, file_path):
        img = Image.open(file_path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.face_image_label.config(image=img)
        self.face_image_label.image = img

    def login(self):
        if self.known_face_encoding is None:
            messagebox.showwarning("Error", "Please browse an image for face recognition.")
            return

        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()

        if not all([name, age, gender]):
            messagebox.showwarning("Error", "Please fill in all fields.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, "w") as file:
                file.write(f"Name: {name}\n")
                file.write(f"Age: {age}\n")
                file.write(f"Gender: {gender}\n")

            messagebox.showinfo("Success", "Information saved successfully.")
            self.clear_fields()
        else:
            messagebox.showwarning("Error", "Please provide a valid file path.")

    def clear_fields(self):
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.label_result.config(text="")
        self.face_image_label.config(image="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionLoginApp(root)
    root.mainloop()
