import tkinter
import tkinter.messagebox

class KiloConverter():
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.prompt_label = tkinter.Label(self.top_frame, text = " Enter a distance in kilometers")
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side = "left")
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        self.calc_button.pack()
        self.quit_button.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def convert(self) -> None:
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        tkinter.messagebox.showinfo("Results", str(kilo) + " kilometers is equal to " + str(miles) + " miles.")
converter = KiloConverter()

    
    