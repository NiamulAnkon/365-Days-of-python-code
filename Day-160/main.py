import yfinance as yf
from tkinter import *


root = Tk()
root.title("Stock Market")
root.geometry("800x800")

def stock_details():
    compony = yf.Ticker("MSFT")
    stock_data = compony.history(period="2mo")
    stock_text = str(stock_data)
    stock_lable.config(text=stock_text)


Stock_btn = Button(root, text="Show Details", command=stock_details, bg="Black", fg="White")
Stock_btn.pack()

stock_lable = Label(root, text="")
stock_lable.pack()

root.mainloop()