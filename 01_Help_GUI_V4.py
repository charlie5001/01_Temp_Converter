from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self, parent):
        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=1200,  height=1200, bg=background_color)
        self.converter_frame.grid()
        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=("Arial 16 bold"),
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
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):
        background = "orange"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #sets up child window ie help box
        self.help_box = Toplevel()

        #If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

        #set up gui frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()
        #set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)
        #dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame,
                            text="Dismiss", font=("Arial 10 bold"),
                            padx=10, pady=10, 
                            command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)
    def close_help(self, partner):
        #Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()