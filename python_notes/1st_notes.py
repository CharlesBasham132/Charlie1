from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
      super().__init__()

    # set window properties
      self.title("Newsletter")
      self.configure(bg="grey", height=600,
                   width=600)

    #add components
      self.__add_outer_frame()
      self.__add_heading_label()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.place(x=10, y=10, relheight = 0.84, relwidth=0.94)

    def __add_heading_label(self):
        #create
        self.heading_label = Label(self.outer_frame)
        #position
        self.heading_label.grid(row = 1,
                                column = 1)
        #style
        self.heading_label.configure(font = "Arial 20",
                                     text = "Template")



my_gui = Gui()
my_gui.mainloop()
