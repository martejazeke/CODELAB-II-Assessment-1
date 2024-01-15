from tkinter import *

root = Tk()

root.geometry("800x800")
root.resizable(False, False)

root.configure(bg="red")

welcome = Label(root, text="Welcome to the window!", bg="Blue", fg= "white", font = ("Arial", 25, "bold"))
welcome.pack()

root.mainloop()
