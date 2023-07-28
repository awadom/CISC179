import tkinter as tk


class FarLeft(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the Label widgets
        self.label1 = tk.Label(self, text="Label 1")
        self.label2 = tk.Label(self, text="Label 2")

        # Pack the widgets to the left (west)
        self.label1.pack(anchor="w")
        self.label2.pack(anchor="w")


if __name__ == "__main__":
    app = FarLeft()
    app.mainloop()
