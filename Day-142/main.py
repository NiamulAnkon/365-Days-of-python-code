import tkinter
from tkinter import *
from textblob import TextBlob


root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word = entry_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root, text="Correct text is: ", font=("poppins",20),bg="#dae6f6", fg="#365971")
    cs.place(x=100,y=250)
    spelling.config(text=right)


heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

entry_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
entry_text.pack(pady=10)
entry_text.focus()

button = Button(root, text="Check", font=("arial", 20, "bold"), fg="White", bg="red", command=check_spelling)
button.pack()


spelling = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spelling.place(x=350, y=250)










root.mainloop()
