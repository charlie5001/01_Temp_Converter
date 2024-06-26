
from tkinter import *
from functools import partial
import random
import re
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

        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                        text="Calculation History", width=15, command=lambda: self.history(self.all_calculations))
        self.history_button.grid(row=0, column=0)
        if len(self.all_calculations) == 0:
            self.history_button.config(state=DISABLED)
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

            if has_errors != "yes":
                self.all_calculations.append(answer)
                print(self.all_calculations)
                self.history_button.config(state=NORMAL)
        


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




    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"

        #disable history button
        partner.history_button.config(state=DISABLED)

        #sets up child window ie history box
        self.history_box = Toplevel()

        #If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))

        #set up gui frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()
        #set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #history text (label, row 1)
        self.history_text = Label(self.history_frame, 
                                  text="Here are your most recent "
                                  "calculations. Please use the "
                                  "the export button to create a text "
                                  "file of all your calculations for this session",
                                  font="arial 10 italic",
                                  justify=LEFT, width=40, fg="maroon",bg=background, wrap=250)
        self.history_text.grid(row=1)
        #History output (row 2)

        #Genreate string from list of calculations
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"
        
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is you calcualtion "
                                            "history. You can use the "
                                            "export button to save this data "
                                            "to a text file if desired."
                                         )
        #Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        #Export / Dismiss Button Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        #Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export", font="Arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        #Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        #Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()
    def export(self, calc_history):
        Export(self, calc_history)
class Export:
    def __init__(self, partner, calc_history):
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
        self.save_button = Button(self.save_cancel_frame, text= "Save", command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)
    def close_export(self, partner):
        #Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
    def save_history(self, partner, calc_history):
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
            
            else: 
                problem = ("no {}'s allowed".format(letter))
            has_error = "yes"
            break
        if filename == "":
            problem = "can't ne blank"
            has_error = "yes"

        if has_error == "yes":
            #Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            #Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        
        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            for item in calc_history:
                f.write(item + "\n")

            f.close()

            self.close_export(partner)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()