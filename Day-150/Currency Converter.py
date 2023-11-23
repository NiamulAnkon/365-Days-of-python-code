import tkinter as tk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")
        self.master.geometry("400x500")

        # Initialize currency converter
        self.currency_converter = CurrencyRates()

        # Create GUI elements
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        self.from_currency_label = tk.Label(self.master, text="From Currency:")
        self.from_currency_label.pack(pady=10)
        self.from_currency_entry = tk.Entry(self.master, textvariable=self.from_currency_var)
        self.from_currency_entry.pack(pady=5)

        self.to_currency_label = tk.Label(self.master, text="To Currency:")
        self.to_currency_label.pack(pady=10)
        self.to_currency_entry = tk.Entry(self.master, textvariable=self.to_currency_var)
        self.to_currency_entry.pack(pady=5)

        self.amount_label = tk.Label(self.master, text="Amount:")
        self.amount_label.pack(pady=10)
        self.amount_entry = tk.Entry(self.master, textvariable=self.amount_var)
        self.amount_entry.pack(pady=5)

        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="Result:")
        self.result_label.pack(pady=5)
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, state="readonly")
        self.result_entry.pack(pady=5)

    def convert_currency(self):
        try:
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            amount = self.amount_var.get()

            result = self.currency_converter.convert(from_currency, to_currency, amount)
            self.result_var.set(result)

        except CurrencyRates.RatesNotAvailableError:
            tk.messagebox.showerror("Error", f"Exchange rates not available for {from_currency} to {to_currency}.")
    
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
