from tkinter import *
from functools import partial
import random


class Converter:
    def __init__(self, parent):
        # Formatting variables...
        background_color = "light blue"

        #Initialse list to hold calcuation history
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
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be "
                                             "converted and then push "
                                             "one of the buttons below...",
                                             font="Arial 10 italic", wrap=250, justify=LEFT, bg = background_color, padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        #conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centigrade", font="Arial 10 bold", bg="yellow", padx=10, pady=10, command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Farhenheit", font="Arial 10 bold", bg="pink", padx=10, pady=10, command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)
        #Answer Label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 12 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        #History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist__button = Button(self.hist_help_frame, font="Arial 12 bold",
                                        text="Calculation History", width=15)
        self.calc_hist__button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"

        #Retrieve amount entered into Entry Fiel d
        to_convert = self.to_convert_entry.get()

        
        #Check amount is a valid number
        try:
            to_convert = float(to_convert)
            has_errors = "no"
        #Convert to F
            if low == -273 and to_convert >= low:
                farhenheit = (to_convert * 9/5 ) + 32
                to_convert = self.round_it(to_convert)
                farhenheit = self.round_it(farhenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, farhenheit)
        #Convert to C

            elif low == -459 and to_convert >= low:
                celcius = (to_convert - 32 ) * 5/9
                to_convert = self.round_it(to_convert)
                celcius = self.round_it(celcius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celcius)

            else:
                answer = "Too Cold"
                has_errors = "yes"
            #Display answer

            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            if answer != "Too Cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)
                


        #Add answer to list for History
        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded
    def to_deg(self):
        which = 1
        self.change(which)

    def to_far(self):
        which = 2
        self.change(which)
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()