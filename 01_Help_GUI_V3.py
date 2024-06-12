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
        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=("Arial", "16", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
        # Help Button (row 1)
        self.help_button = Button(self.converter_frame,
                                  text="Help", font=("Arial", "14"),
                                  padx=10, pady=10, 
                                  command=self.help)
    
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = help(self)
        get_help.help_text.configure(text="Help text goes here")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()