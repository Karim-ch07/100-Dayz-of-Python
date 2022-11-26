from tkinter import *
from pandas import *
from random import *
from tkinter import messagebox
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- GAME LOGIC ------------------------------- #

data = read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")


def gen_card():
    current_pair = choice(to_learn)
    canvas.itemconfig(text_word, text=current_pair["French"])
    canvas.itemconfig(text_title, text="French")


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas

img_card_front = PhotoImage(file="./images/card_front.png")
# img_card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=img_card_front)
text_title = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
text_word = canvas.create_text(400, 250, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button

img_right = PhotoImage(file="./images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=gen_card)
button_right.grid(column=1, row=1)

img_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=gen_card)
button_wrong.grid(column=0, row=1)

gen_card()

window.mainloop()
