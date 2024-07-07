import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.currency_rates = CurrencyRates()

        self.label_amount = tk.Label(master, text="Amount:")
        self.label_amount.grid(row=0, column=0, padx=10, pady=10)

        self.entry_amount = tk.Entry(master)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10)

        self.label_from = tk.Label(master, text="From Currency:")
        self.label_from.grid(row=1, column=0, padx=10, pady=10)

        self.from_currency = tk.StringVar(master)
        self.from_currency.set("USD")  # default value
        self.option_from = tk.OptionMenu(master, self.from_currency, "USD", "EUR", "GBP", "INR")
        self.option_from.grid(row=1, column=1, padx=10, pady=10)

        self.label_to = tk.Label(master, text="To Currency:")
        self.label_to.grid(row=2, column=0, padx=10, pady=10)

        self.to_currency = tk.StringVar(master)
        self.to_currency.set("EUR")  # default value
        self.option_to = tk.OptionMenu(master, self.to_currency, "USD", "EUR", "GBP", "INR")
        self.option_to.grid(row=2, column=1, padx=10, pady=10)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=3, columnspan=2, padx=10, pady=10)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            amount = float(self.entry_amount.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            result = self.currency_rates.convert(from_curr, to_curr, amount)
            self.label_result.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
        except ValueError:
            self.label_result.config(text="Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
