from tkinter import *
class MyWindow:
    def __init__(self,win):


        self.lbl = Label(win, text="Compute for Simple or Compound Amount", bg="#87CEEB", fg="#FFA500")
        self.lbl.place (x=120, y=10)
        self.lbl1 = Label(win,text="Insert time (in years)", fg="#FFA500", bg="#87CEEB")
        self.lbl1.place(x=10,y=50)
        self.lbl2 = Label(win, text= "Insert rate of interest (in a year)",  fg="#FFA500", bg="#87CEEB")
        self.lbl2.place(x=10,y=100)
        self.lbl4 = Label(win, text = "Amount of Interest", fg="#FFA500", bg="#87CEEB")
        self.lbl4.place(x=10, y=250)
        self.lbl3 = Label(win, text="Insert the principal (Amount of Money borrowed or deposited)",fg="#FFA500", bg="#87CEEB")
        self.lbl3.place(x=10,y=150)
        self.lbl6 = Label(win, text="Insert the value of (n) number of the interest is compounded annually", fg="#FFA500", bg="#87CEEB")
        self.lbl6.place(x=10, y=200)
        self.lbl5 = Label(win, text="(e.g. Annually = 1, Quarterly = 4, Bi-Annually/SemiAnnual = 2)", fg="#FFA500", bg="#87CEEB")
        self.lbl5.place(x=10, y=220)
        self.lbl7 = Label(win, text="Compute for the Markdown or Markup percentage", fg="#FFA500", bg="#87CEEB")
        self.lbl7.place(x=120, y=360)
        self.lbl8 = Label(win, text="Input original price", fg="#FFA500", bg="#87CEEB")
        self.lbl8.place(x=10, y=400)
        self.lbl9 = Label(win, text="Input selling price", fg="#FFA500", bg="#87CEEB")
        self.lbl9.place(x=10, y=450)
        self.lbl10 = Label(win, text="Markdown/Markup Percentage", fg="#FFA500", bg="#87CEEB")
        self.lbl10.place(x=10, y=500)
        self.MorUPer = Entry(win, bd=1)
        self.MorUPer.place(x=400,y=500)
        self.OrigP = Entry(win, bd=1)
        self.OrigP.place(x=400, y=400)
        self.SellP = Entry(win, bd=1)
        self.SellP.place(x=400,y=450)
        self.time = Entry(win,bd=1)
        self.time.place(x=400,y=50)
        self.Irate = Entry(win,bd=1)
        self.Irate.place(x=400,y=100)
        self.PrinciA = Entry(win,bd=1)
        self.PrinciA.place(x=400,y=150)
        self.CorIinterest = Entry(win,bd=3)
        self.CorIinterest.place(x=400, y=250)
        self.n = Entry(win, bd=1)
        self.n.place(x=400, y=200)
        self.btnSint = Button(win,text="Simple Interest", command=self.simpleI)
        self.btnSint.place(x=10,y=300)
        self.btnCint = Button(win,text="Compound Interest", fg = "Orange",command = self.compoundI)
        self.btnCint.place(x=150,y=300)
        self.btnDrate = Button(win,text="Mark-down rate", fg="Light Blue",command=self.MDRate)
        self.btnDrate.place(x=10,y=600)
        self.btnUrate = Button(win, text="Mark-up rate", fg="Red",command=self.MURate)
        self.btnUrate .place(x=150,y=600)
        self.btnclear = Button(win, text="Clear Everything", fg="Green",command=self.clear)
        self.btnclear.place(x=400, y=650)





    def simpleI(self):
        self.CorIinterest.delete(0,'end')
        t = float(self.time.get())
        r = float(self.Irate.get())
        p = float(self.PrinciA.get())
        SimpIA = t*r*p
        self.CorIinterest.insert(END,str(SimpIA))


    def compoundI(self):
        self.CorIinterest.delete(0, 'end')
        t = float(self.time.get())
        r = float(self.Irate.get())
        p = float(self.PrinciA.get())
        n = float(self.n.get())
        CompIA = p*((1+(r/n))**(t*n))
        self.CorIinterest.insert(END,str(CompIA))

    def MDRate(self):
        self.MorUPer.delete(0, 'end')
        origP = float(self.OrigP.get())
        sellP = float(self.SellP.get())
        MarkDorU = 100*(((sellP-origP)/origP)*(-1))
        self.MorUPer.insert(END, str(MarkDorU))

    def MURate(self):
        self.MorUPer.delete(0, 'end')
        origP = float(self.OrigP.get())
        sellP = float(self.SellP.get())
        MarkDorU = 100 * ((sellP - origP)/origP)
        self.MorUPer.insert(END, str(MarkDorU))

    def clear(self):
        self.MorUPer.delete(0, 'end')
        self.OrigP.delete(0, 'end')
        self.SellP.delete(0, 'end')
        self.time.delete(0, 'end')
        self.Irate.delete(0, 'end')
        self.PrinciA.delete(0, 'end')
        self.CorIinterest.delete(0, 'end')
        self.n.delete(0, 'end')




window = Tk()
mywin = MyWindow(window)
window.geometry("600x1000")
window.title("Finance Calculator")
window.configure(bg="#87CEEB")
window.mainloop()








