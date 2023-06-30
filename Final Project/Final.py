import tkinter as tk
from tkinter import filedialog, messagebox
import csv


def process_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    stock_data = {}
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = row["Date"]
            month = date.split("/")[0]  # Extract the month from the date
            for stock, price in row.items():
                if stock != "Date":
                    if stock not in stock_data:
                        stock_data[stock] = {}
                    if month not in stock_data[stock]:
                        stock_data[stock][month] = {
                            "high": float(price),
                            "low": float(price),
                        }
                    else:
                        if float(price) > stock_data[stock][month]["high"]:
                            stock_data[stock][month]["high"] = float(price)
                        if float(price) < stock_data[stock][month]["low"]:
                            stock_data[stock][month]["low"] = float(price)

    formatted_data = ""
    for stock, data in stock_data.items():
        formatted_data += f"{stock}\n"
        formatted_data += f'{"Month": <10}{"High Price": <12}{"Low Price"}\n'
        formatted_data += "-" * 34 + "\n"
        for month, prices in data.items():
            formatted_data += (
                f'{month: <10}{prices["high"]: <12.2f}{prices["low"]: <12.2f}\n'
            )
        formatted_data += "\n"

    messagebox.showinfo("Stock Data", formatted_data)


root = tk.Tk()
root.title("Dow Jones Stock Prices")

button = tk.Button(root, text="Open CSV", command=process_csv)
button.pack()

root.mainloop()
