import tkinter as tk


class LabelMaker(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the main window attribute
        self.main_window = self

        # Create the Label widget
        label_widget = tk.Label(self.main_window, text="Programming is fun!")
        label_widget.pack()


if __name__ == "__main__":
    app = LabelMaker()
    app.mainloop()
