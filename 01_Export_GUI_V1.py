from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self, parent):
        # Formatting variables...
        background_color = "light blue"


        self.all_calculations = []
        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300,  height=1200, bg=background_color)
        self.converter_frame.grid()
        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=("Arial 16 bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
        #User Instructions row(1)


        #Temperature entry box (row 2)


        #conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)


        #Answer Label (row 4)

        #export / export button frame (row 5)
        self.export_button = Button(self.converter_frame,
                                  text="export", font=("Arial", "14"),
                                  padx=10, pady=10, 
                                  command=self.export)
    
        self.export_button.grid(row=1)
 
    def export(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):
        background = "#a9ef99"

        #disable export button
        partner.export_button.config(state=DISABLED)

        #sets up child window ie export box
        self.export_box = Toplevel()

        #If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol("WM_DELETE_WINDOW", partial(self.close_export, partner))

        #set up gui frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()
        #set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="export / Instructions",font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file", 
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)
        #dismiss button (row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists it contents will be replaced with your calculation", 
                                 justify=LEFT, width=40, bg=background, wrap=225, padx=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        #Save / Cancel Frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        #Save and Cancel Buttons
        self.save_button = Button(self.save_cancel_frame, text= "Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)
    def close_export(self, partner):
        #Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()