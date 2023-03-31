from tkinter import *
windows = Tk()
label1 = Label (windows, text = "My first application", fg = "Red", font= ("Verdana", 20))
label1.place(x=130,y=15)
label2 = Label (windows,text="Name: ", fg="Light Blue", font="Tahoma")
label2.place(x=130,y=80)
label3 = Label (windows, text="Age: ", fg = "Light Blue", font = "Tahoma")
label3.place(x=130, y=120)
label4 = Label (windows, text="Birthdate", fg="Light Blue", font="Tahoma")
label4.place(x=130, y=160)

txtfldl = Entry(windows,bd=2)
txtfldl.place(x=200, y=80)
txtfldl2 = Entry(windows, bd=2)
txtfldl2.place(x=200, y=120)
txtfldl3 = Entry(windows, bd=2)

windows.geometry ("500x400+10+10")

windows.mainloop()