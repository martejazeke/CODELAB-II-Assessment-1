from tkinter import *
from tkinter import messagebox

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        
    def calcGrade(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        return avg 
    
    def display(self):
        avg = self.calcGrade()
        return f"Hello, {self.name}! Your average grade is {avg}"
    
class StudentGUI(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Student Information")
        self.geometry("300x400")
        
        self.input_values()
        
    def input_values(self):
        name_label = Label(self, text = "Enter the student's name: ")
        name_label.pack()
        name_entry = Entry(self)
        name_entry.pack(pady=5)
        
        mark1_label = Label(self, text = "Enter Mark 1: ")
        mark1_label.pack()
        mark1_entry = Entry(self)
        mark1_entry.pack(pady=5)
        
        mark2_label = Label(self, text = "Enter Mark 2: ")
        mark2_label.pack()
        mark2_entry = Entry(self)
        mark2_entry.pack(pady=5)
        
        mark3_label = Label(self, text = "Enter Mark 3: ")
        mark3_label.pack()
        mark3_entry = Entry(self)
        mark3_entry.pack(pady=5)

        submit_button = Button(self, text = "Submit", command=lambda:self.display_result(name_entry.get(), int(mark1_entry.get()) , int(mark2_entry.get()) , int(mark3_entry.get())))
        submit_button.pack(pady=10)
        
    def display_result(self, name, mark1, mark2, mark3):
        student = Student(name, mark1, mark2, mark3)
        result_label = Label(self, text = student.display())
        result_label.pack(pady=10)
        
if __name__ == "__main__":
    app = StudentGUI()
    app.mainloop()