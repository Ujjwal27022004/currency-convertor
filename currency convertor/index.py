import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
from ttkthemes import ThemedStyle

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        style = ThemedStyle(root)
        style.set_theme("equilux") 
        
        self.currency_rates = CurrencyRates()

        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.pack()

        self.from_currency_var = tk.StringVar()
        self.from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var, values=list(self.currency_rates.get_rates("").keys()))
        self.from_currency_combobox.pack()

        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.pack()

        self.to_currency_var = tk.StringVar()
        self.to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var, values=list(self.currency_rates.get_rates("").keys()))
        self.to_currency_combobox.pack()

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.pack()

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack()

    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_entry.get())

        try:
            conversion_rate = self.currency_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * conversion_rate
            self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        except:
            self.result_label.config(text="Error converting currencies.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
