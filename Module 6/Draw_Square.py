import tkinter


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        self.canvas.create_rectangle(20, 20, 180, 180)
        self.canvas.create_polygon(
            60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60
        )
        self.canvas.create_arc(10, 10, 190, 190, start=45, extent=30)
        self.canvas.create_oval(20, 20, 70, 70)
        self.canvas.create_oval(100, 100, 180, 130)
        self.canvas.pack()
        tkinter.mainloop()


my_gui = MyGUI()
