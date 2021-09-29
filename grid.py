from tkinter import *

mw = Tk()

mylabel1 = Label(mw, text='Tharun', font=('Arial', 20), fg='red', bg='#03fcd7')            #fg=fornt ground
mylabel2 = Label(mw, text='sagar', font=('Arial', 20))
mylabel3 = Label(mw, text='madhu', font=('Arial', 20))
mylabel4 = Label(mw, text='shiva', font=('Arial', 20))

mybutton = Button(mw,text='click me!', font=('Arial',10), bg='#03fcd7',fg='blue')       #bg=background,  #google: color picker

mylabel1.grid(row=0, column=0, padx=20)
mylabel2.grid(row=1, column=1)
mylabel3.grid(row=2, column=2)
mylabel4.grid(row=0, column=3)
mybutton.grid(row=2, column=1,pady=30)

mw.mainloop()
