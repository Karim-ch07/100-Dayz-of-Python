import tkinter
# from tkinter import *

window = tkinter.Tk()
window.title("Learning GUI")
window.minsize(width=500, height=300)

#Label

MyLabel = tkinter.Label(text="This is a test label.", font=("Arial", 24, "bold"))
MyLabel.pack()

MyLabel['text'] = "New test label."
MyLabel.config(text="New test label 2.0.")

#Button

def button_clicked():
    # print("Clickkkkking!")
    MyLabel.config(text=f"Button got clicked!")

# button = tkinter.Button(text="Click me!", command=button_clicked)
# button.pack()

#Entry

def read_write_input():
    MyLabel.config(text=input.get())

button = tkinter.Button(text="Click me!", command=read_write_input)
button.pack()

input = tkinter.Entry(width=30)
input.pack()

window.mainloop()
