from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_date():
    with open("data.txt", "a") as file:
        file.write(f"Website: {input_website.get()}\t|\tEmail/Username: {input_email.get()}\t|\tPassword: {input_pw.get()}\n")

    input_website.delete(0, END)
    input_website.focus()
    # input_email.delete(0, END)
    input_pw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

# Canvas

img_png = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_png)
canvas.grid(column=1, row=0)

# Label

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_pw = Label(text="Password:")
label_pw.grid(column=0, row=3)

# Input

input_website = Entry(width=59)
input_website.grid(column=1, row=1, columnspan=2)

input_email = Entry(width=59)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, string="sample.sample@email.com")

input_pw = Entry(width=34)
input_pw.grid(column=1, row=3)

# Button

button_generate = Button(text="Generate Password", width=20, highlightthickness=0, command=generate_pw)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=50, highlightthickness=0, command=save_date)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()