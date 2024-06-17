from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self, parent):
        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=309, bg=background_color)
        self.converter_frame.grid()
        #Temperature Conversion Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=("Arial 16 bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)
        
        #User Instructions row(1)
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be "
                                             "converted and then push "
                                             "one of the buttons below...",
                                             font="Arial 10 italic", wrap=250, justify=LEFT, bg = background_color, padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #Temperature entry box (row 2)

        #conversion buttons frame (row 3)
    
        #Answer Label (row 4)

        #History / Help button frame (row 5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()