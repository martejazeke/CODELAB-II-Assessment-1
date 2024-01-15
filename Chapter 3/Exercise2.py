from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def update_order():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    messagebox.showinfo('Order', f"Your order is a {coffee} with {sugar} sugar and {milk} milk.")

#Main Frame

root = Tk()
root.title("Coffee Vending Machine")
root.resizable(False, False)

#Frame

frame = Frame(root, bg = "#BE9B7B")
frame.pack(padx=10)

#logo

img = Image.open("coffeelogo.png")
logo = ImageTk.PhotoImage(img.resize((100,100)))

logo_label = Label(frame, image=logo, bg="#BE9B7B")
logo_label.pack(padx=10)

#Title

title = Label(frame, text="BSU Cafe", bg="#BE9B7B", fg="black", font=("Helvetica", 15, "bold"))
title.pack(padx=10)

#coffee

coffee_var = StringVar()

coffee_label = Label(frame, text = "•     DRINKS     •", bg="#6F4436", fg="white", font=("Helvetica", 12, "bold"), padx= 10, pady=10).pack(padx=10, pady=10)

#Latte

img1 = Image.open("latte.png")
latte = ImageTk.PhotoImage(img1.resize((100,100)))

latte_label = Label(frame, image=latte, bg="#BE9B7B")
latte_label.pack(side="left", padx=24)

latte_text = Radiobutton(frame, text="Latte", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold" ), variable=coffee_var, value="latte")
latte_text.pack(side="left")

#Mocha

img2 = Image.open("mocha.png")
mocha = ImageTk.PhotoImage(img2.resize((100,100)))

mocha_label = Label(frame, image=mocha, bg="#BE9B7B")
mocha_label.pack(side = "left", padx=10)

mocha_text = Radiobutton(frame, text="Mocha", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="mocha", padx=10)
mocha_text.pack(side="left")

#Cappuccino

frame2 = Frame(root, bg="#BE9B7B")
frame2.pack(padx=10)

img3 = Image.open("cappuccino.png")
cap = ImageTk.PhotoImage(img3.resize((100,100)))

cap_label = Label(frame2, image=cap, bg="#BE9B7B")
cap_label.pack(side="left", padx=10)

cap_text = Radiobutton(frame2, text="Cappuccino", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="cappuccino")
cap_text.pack(side="left")

#Hot Chocolate

img4 = Image.open("hotchoco.png")
hotchoco = ImageTk.PhotoImage(img4.resize((100,100)))

hotchoco_label = Label(frame2, image=hotchoco, bg="#BE9B7B")
hotchoco_label.pack(side="left")

hotchoco_text = Radiobutton(frame2, text="Hot Choco", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="hot choco")
hotchoco_text.pack(side="left")

#Sugar

frame3 = Frame(root, bg ="#BE9B7B")
frame3.pack()

sugar_var = StringVar()

sugar_label = Label(frame3, text = "•      SUGAR      •", bg="#6F4436", fg="white", font=("Helvetica", 12, "bold"), padx= 10, pady=10)
sugar_label.pack(padx=142, pady=20)

zero = Radiobutton(frame3, text="0%", bg="#BE9B7B", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="no")
zero.pack(side="left", padx=20)

twenty_five = Radiobutton(frame3, text="25%", bg="#BE9B7B", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="25%")
twenty_five.pack(side="left", padx=20)

fifty = Radiobutton(frame3, text="50%", bg="#BE9B7B", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="50%")
fifty.pack(side="left", padx=20)

seventy_five = Radiobutton(frame3, text="75%", bg="#BE9B7B", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="75%")
seventy_five.pack(side="left", padx=20)

#Milk

frame4 = Frame(root, bg="#BE9B7B")
frame4.pack()

milk_var = StringVar()

milk_label =Label(frame4, text = "•         MILK         •", bg="#6F4436", fg="white", font=("Helvetica", 12, "bold"), padx= 10, pady=10)
milk_label.pack(padx=20, pady=20)

skimmed = Radiobutton(frame4, text="Skimmed", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="skimmed")
skimmed.pack(side="left", padx=20)

almond = Radiobutton(frame4, text="Almond", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="almond")
almond.pack(side="left", padx=12)

oat = Radiobutton(frame4, text="Oat", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="oat")
oat.pack(side="left", padx=12)

low_fat = Radiobutton(frame4, text="Low Fat", bg="#BE9B7B", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="low fat")
low_fat.pack(side="left", padx=20)

#Order

frame5 = Frame(root, bg="#BE9B7B")
frame5.pack()

order_button = Button(frame5, text="ORDER", bg="#3C2F2F", fg="white", font=("Helvetica", 12, "bold"), padx= 10, pady=5, bd=0, command= update_order)
order_button.pack(padx=169, pady=10)

order_text = Label(frame5, text="", bg="#BE9B7B", font=("Helvetica", 10))
order_text.pack(pady=10)


root.mainloop()


