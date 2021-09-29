from tkinter import *

mw = Tk()


def say_hello():
    name = userinput.get()  # give text of input
    greeting = 'hello ' + name + ' !'
    if name != '':
        my_text.config(text=greeting)  # config will over ride
        userinput.delete(0, END)


userinput = Entry(mw, width=20, font=('Arial', 18))
userinput.pack(padx=10, pady=10)

my_text = Label(mw, text='Enter your Name:', font=('Arial', 14))
my_text.pack(pady=5)

btn = Button(mw, text='say hello!', font=('Arial', 12), command=say_hello)
btn.pack(pady=20)

mw.mainloop()
