from tkinter import *

# creating window
main_window = Tk()


def clicked():
    mylabel = Label(main_window, text="i love telugu computer world", font=('Arial', 12))
    mylabel.pack(pady=10)


# creating inputs
user_input = Entry(main_window, width=15, font=('Arial', 18))  # instead of padx:width pady:font
user_input.pack(pady=30)

# creating buttons
my_button = Button(main_window, text="click me!", padx=20, pady=10, font=('Arial', 14), command=clicked)
my_button.pack(padx=50, pady=50)

main_window.mainloop()
