from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="yellow",
                       height=500,
                       width=500)

        self.add_heading_label()
        self.add_instruction_label()

        self.add_advance_button()

    def add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.place(x=0, y=0)

        #style
        self.heading_label.configure(font = "Arial 24",
                                     text = "Recieve our Newsletter")

    def add_instruction_label (self):
        self.instruction_label = Label()
        self.instruction_label.place(x=0, y=50)

        self.instruction_label.configure(font = "Arial 16",
                                         text = "Please enter your detalis")
                                         

    def add_advance_button(self):
        self.advance_button = Button()
        self.advance_button.place(x=0, y=100)

        self.advance_button.configure(bg="red",
                                      text ="subscribe",
                                      width=50)
    


        

gui = Gui()
gui.mainloop()