from tkinter import *
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