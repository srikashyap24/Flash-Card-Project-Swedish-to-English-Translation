BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import random
from tkinter import *


df=pd.read_csv("data/flashcarddata.csv")
data=df.to_dict(orient="records")
current_card={}

def nextcard():
    global current_card,window_timer
    window.after_cancel(window_timer)
    current_card=random.choice(data)
    canvas.itemconfig(card_title,text="Swedish",fill="black")
    canvas.itemconfig(card_word,text=current_card["Swedish"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    window_timer=window.after(4000, func=flipcard)


def flipcard():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

window=Tk()
window.title("Flash Cards!")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

window_timer=window.after(4000,func=flipcard)

canvas=Canvas(width=800, height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263, image=card_front_img)
card_title=canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"),fill="black")
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0)

unknown_button=Button(text="Next",highlightthickness=0,font=("Ariel",60,"bold"), command=nextcard )
unknown_button.grid(row=1,column=0,)

nextcard()


window.mainloop()