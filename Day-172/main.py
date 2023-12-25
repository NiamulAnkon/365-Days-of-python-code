import os
import tkinter as tk
from tkinter import filedialog
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from shutil import copyfile

class ImageRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Recognition and Sorting Tool")
        self.master.geometry("400x200")

        self.src_folder = tk.StringVar()
        self.dest_folder = tk.StringVar()

        self.label_src = tk.Label(self.master, text="Source Folder:")
        self.label_src.pack()

        self.entry_src = tk.Entry(self.master, textvariable=self.src_folder, state="readonly")
        self.entry_src.pack()

        self.button_src = tk.Button(self.master, text="Select Source Folder", command=self.select_source_folder)
        self.button_src.pack()

        self.label_dest = tk.Label(self.master, text="Destination Folder:")
        self.label_dest.pack()

        self.entry_dest = tk.Entry(self.master, textvariable=self.dest_folder, state="readonly")
        self.entry_dest.pack()

        self.button_dest = tk.Button(self.master, text="Select Destination Folder", command=self.select_destination_folder)
        self.button_dest.pack()

        self.button_sort = tk.Button(self.master, text="Sort Images", command=self.sort_images)
        self.button_sort.pack()

    def select_source_folder(self):
        folder_selected = filedialog.askdirectory()
        self.src_folder.set(folder_selected)

    def select_destination_folder(self):
        folder_selected = filedialog.askdirectory()
        self.dest_folder.set(folder_selected)

    def sort_images(self):
        source_folder = self.src_folder.get()
        destination_folder = self.dest_folder.get()

        if not source_folder or not destination_folder:
            tk.messagebox.showwarning("Folder Selection", "Please select both source and destination folders.")
            return

        # Load pre-trained MobileNetV2 model
        model = MobileNetV2(weights='imagenet')

        for filename in os.listdir(source_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(source_folder, filename)
                img = image.load_img(image_path, target_size=(224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = preprocess_input(img_array)

                predictions = model.predict(img_array)
                decoded_predictions = decode_predictions(predictions, top=1)[0]
                predicted_label = decoded_predictions[0][1]

                category_folder = os.path.join(destination_folder, predicted_label)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination_path = os.path.join(category_folder, filename)
                copyfile(image_path, destination_path)

        tk.messagebox.showinfo("Sorting Complete", "Images have been sorted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageRecognitionApp(root)
