from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

equal = Label(text="is equal to")
equal.grid(row=2, column=1)

miles = Label(text="Miles")
miles.grid(row=1, column=3)

km = Label(text="km")
km.grid(row=2, column=3)

calculated = Label(text="0")
calculated.grid(row=2, column=2)

def button_clicked():
    result = float(input.get())
    kilometers = result * 1.609
    calculated.config(text=f"{kilometers}")

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

input = Entry(width=10)
input.grid(row=1, column=2)


window.mainloop()
