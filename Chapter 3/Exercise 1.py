from tkinter import *

def update_greet():
    name = name_entry.get()
    color = color_var.get()
    greet_label.config(text=f"Hello, {name}!", fg = color)
    
#Main Window

root = Tk()

#InputFrame

InFrame = Frame(root, bg="#c7dfff")
InFrame.pack(padx=10, pady=10)

title = Label(InFrame, text="Input Frame", bg="#c7dfff", fg="black", font=("Arial", 15, "bold"), padx=10, pady=10)
title.pack()

name = Label(InFrame, text = "Enter your name: ", bg="#c7dfff", fg="black", font=("Arial", 10, "bold"), padx=10, pady=10)
name.pack()

name_entry = Entry(InFrame)
name_entry.pack()

color_label = Label(InFrame, text="Choose a color: ", bg="#c7dfff", fg="black", font=("Arial", 10, "bold"), padx=15, pady=5)
color_label.pack()

colors = ["red", "yellow", "blue", "lightgreen", "pink"]
color_var = StringVar()
dropdown = OptionMenu(InFrame, color_var, *colors)
dropdown.configure(border=0)
color_var.set("red") #sets the default color
dropdown.pack(pady=10)

update = Button(InFrame, text="Update Greeting", command = update_greet)
update.pack(pady=10)

#Display Frame

DisplayFrame = Frame(root)
DisplayFrame.pack(padx=10, pady=10)

display_title = Label(DisplayFrame, text="Display Greeting", bg="#c7ffd4", font=("Arial", 10, "bold"), fg="black", padx=10, pady=10)
display_title.pack()

greet_label = Label(DisplayFrame, text=" ", bg="#c7ffd4", fg="black", font=("Arial", 10, "bold"), padx=25)
greet_label.pack()

root.mainloop()

