import tkinter as tk
from tkinter import messagebox

def vote():
    global num1_votes, num2_votes, nomine_1, nomine_2
    voter = int(voter_entry.get())
    
    if voter in voter_id:
        voter_id.remove(voter)
        vote = int(vote_entry.get())

        if vote == 1:
            messagebox.showinfo("Thank you", f"{nomine_1.get()}, thank you for your vote")
            num1_votes += 1
        elif vote == 2:
            messagebox.showinfo("Thank you", f"{nomine_2.get()}, thanks for your vote")
            num2_votes += 1
        elif vote > 2:
            messagebox.showerror("Error", "Check Your Passed key")
        else:
            messagebox.showerror("Error", "Invalid vote")
    else:
        messagebox.showerror("Error", "You are not a voter or you have already voted")

    update_status()

def update_status():
    if len(voter_id) == 0:
        if num1_votes > num2_votes:
            percent = (num1_votes / (num1_votes + num2_votes)) * 100
            result_label.config(text=f"{nomine_1.get()} has won the election with {percent}% votes")
        elif num2_votes > num1_votes:
            percent2 = (num2_votes / (num1_votes + num2_votes)) * 100
            result_label.config(text=f"{nomine_2.get()} has won the election with {percent2}% votes")
        else:
            result_label.config(text="Both are equal, so no one has won the election.")

# Function to create and run the Tkinter application
def create_gui():
    global root, voter_id, num1_votes, num2_votes, nomine_1, nomine_2, voter_entry, vote_entry, result_label

    root = tk.Tk()
    root.title("Election Voting System")
    root.geometry("700x500")

    nomine_1 = tk.StringVar()
    nomine_2 = tk.StringVar()

    nomine_1.set(input("Enter the name of Candidate 1: "))
    nomine_2.set(input("Enter the name of Candidate 2: "))

    num1_votes = 0
    num2_votes = 0

    voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    intro_label = tk.Label(root, text="Your voter ID is going to be 1-10, so you can choose your voter ID between 1-10")
    intro_label.pack()

    name_label = tk.Label(root, text=f"Candidate 1: {nomine_1.get()}\nCandidate 2: {nomine_2.get()}")
    name_label.pack()

    voter_label = tk.Label(root, text="Enter your voter ID:")
    voter_label.pack()
    voter_entry = tk.Entry(root)
    voter_entry.pack()

    vote_label = tk.Label(root, text=f"To vote for {nomine_1.get()}, press 1\nTo vote for {nomine_2.get()}, press 2")
    vote_label.pack()
    vote_entry = tk.Entry(root)
    vote_entry.pack()

    vote_button = tk.Button(root, text="Vote", command=vote)
    vote_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

# Call the function to create and run the Tkinter application
create_gui()
