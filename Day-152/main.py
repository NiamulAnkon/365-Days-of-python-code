import tkinter as tk
import random

class rubikscubescrambler:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Scrambler")
        self.root.geometry("700x300")
        self.root.configure(bg="White")

        self.scramble_list = [
            "F2 D U2 B' U R F2 U B2 F U' L2 R2 U' R D R D2 B2 D' R' F2 L F2 D U2 B2 U L D2",
            "U B U2 L2 F R' U' R2 D' B' U F D U2 F R F U' F D' U2 F' L F' R B U' F' L' U2",
            "D2 R2 B2 D L' D' L2 D B F' D R D B' F2 D L' R' D2 B F2 L' D2 U B D L' R D2 F2",
            "L R' U2 B2 L' D2 F2 L R U L' D B R2 B' F D2 U2 L2 U2 L2 D R' U B2 F' L D F' U'",
            "B F2 U2 L2 B2 R2 B' F2 D B F R B' R U B' L' D' B2 L2 F L' D B2 F R2 U2 L R B'"
        ]

        lable_font = ("Arial", 12)
        btn_font = ("Arial", 15)

        self.scramble_label = tk.Label(root, text="", font=lable_font, bg="White")
        self.scramble_label.pack(pady=10)

        self.scramble_button = tk.Button(root, text="Scramble", command=self.generate_scramble, bg="Red", fg="White", font=btn_font)
        self.scramble_button.pack(side="bottom")

    def generate_scramble(self):
        random_scramble = random.choice(self.scramble_list)
        self.scramble_label.config(text=random_scramble)

if __name__ == "__main__":
    root = tk.Tk()
    app = rubikscubescrambler(root)
    root.mainloop()
