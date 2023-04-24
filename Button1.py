from tkinter import *
class MyWindow:
    def __init__(self,Win4):
        self.btncolor = Button(Win4, text="Color", bg="Blue", fg="Red")
        self.btncolor.place(x=30, y=100)
        self.changebtncolor = Button(Win4, text="<---Click to change the color of the button", command = self.changecolor)
        self.changebtncolor.place(x=80, y=100)
    def changecolor(self):
        self.btncolor = Button (text="Color", bg="Yellow", fg="Red")
        self.btncolor.place(x=30, y=100)

#add event-handling /bind () method
#widgets start from here




window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()