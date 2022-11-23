from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Password Generator")
window.minsize(width=240, height=240)
window.config(padx=20, pady=20)

# Canvas

img_png = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_png)
# text_timer = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
# canvas.grid(column=1, row=1)
canvas.pack() # to be modified later on

# Label

# Input

# Button


window.mainloop()