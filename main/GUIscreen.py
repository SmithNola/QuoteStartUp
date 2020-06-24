from tkinter import *
class GUI:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def create_screen(quote,author):
        screen = Tk()
        frame = Frame(screen)
        frame.pack()
        bottomframe = Frame(screen)
        bottomframe.pack( side = BOTTOM )
        screen.geometry("300x200")#controls the size of the window
        randomButton= Button(bottomframe, text = "New quote")
        randomButton.place(x = 50,y = 50)
        randomButton.pack(side = BOTTOM)
        screen.mainloop()