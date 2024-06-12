from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self, parent):
        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600,  height=600, bg=background_color)
        self.converter_frame.grid()
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()