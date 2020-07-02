from tkinter import *

class GUI:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def create_screen(self, quote, author):
        screen = Tk()
        frame = Frame(screen)
        frame.pack()
        screen.geometry("300x125")  # controls the size of the window
        bottomframe = Frame(screen)
        bottomframe.pack(side=BOTTOM)
        middleframe = Frame(screen)
        middleframe.pack(side=TOP)
        quoteLabel = Label(middleframe, text=quote, wraplength=250)
        authorLabel = Label(middleframe, text="-"+author, wraplength=250)
        quoteLabel.pack(side=TOP)
        authorLabel.pack(side=TOP)
        randomButton = Button(bottomframe, text="New quote")
        randomButton.place(x=50, y=50)
        randomButton.pack(side=BOTTOM)
        screen.mainloop()
