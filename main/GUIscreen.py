from tkinter import *

class GUI:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    # Creates the gui screen displaying quote and author
    def create_screen(self, quote, author):
        screen = Tk()
        frame = Frame(screen)
        frame.pack()
        screen.geometry("300x125")  # controls the size of the window
        middleframe = Frame(screen)
        middleframe.pack(side=TOP)
        quoteLabel = Label(middleframe, text=quote, wraplength=250, bg='#80ccff')
        authorLabel = Label(middleframe, text="-" + author, wraplength=250, bg='#80ccff')
        quoteLabel.pack(side=TOP)
        authorLabel.pack(side=TOP)
        screen.configure(bg='#80ccff')
        middleframe.configure(bg='#80ccff')
        screen.mainloop()