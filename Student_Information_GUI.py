from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class StudentInformationGUI:
    
    def __init__(self, StudentForm):
        
        self.StudentForm = StudentForm
        StudentForm.geometry("800x700")
        StudentForm.title("Student Information Form")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')

        self.bg = PhotoImage(file = "Images/Student Form.png")
        self.Picture = Label(StudentForm, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(StudentForm, width = 550, height = 650, bg = 'LightBlue2')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Student Information", fg = 'Dark Slate Blue', bg = 'LightBlue2', font = self.TitleFont)
        self.title.place(x= 50, y = 10)

        self.FullName = Label(self.frame, text = "Full Name :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.FullName.place(x = 10, y = 100)
        self.Address = Label(self.frame, text = "Address :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Address.place(x = 10, y = 180)
        self.ContactNumber = Label(self.frame, text = "Contact Number :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.ContactNumber.place(x = 10, y =  260)
        self.Grade = Label(self.frame, text = "Grade :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Grade.place(x = 10, y =  340)
        self.Subjects = Label(self.frame, text = "Subjects :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Subjects.place(x = 10, y = 420)

        self.FullNameEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.FullNameEnter.place(x = 80, y = 140)
        self.AddressEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.AddressEnter.place(x = 80, y = 220)
        self.ContactNumberEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.ContactNumberEnter.place(x = 80, y = 300)

        self.clicked = StringVar()
        self.clicked.set("Primary Classes")
        self.GradeEnter = OptionMenu(self.frame, self.clicked, "Primary Classes", "Grade 6", "Grade 7", "Grade 8","Grade 9", "Grade 10", "Grade 11", "Ordinary Level", "Advanced Level", "Adult Classes")
        self.GradeEnter.config(font = self.LableFont, width = 36)
        self.GradeEnter.place(x = 80, y = 380)
        self.menu = self.frame.nametowidget(self.GradeEnter.menuname)
        self.menu.config(font = self.LableFont)

        self.Submit = Button(self.frame, text = "Submit", width = 10, height = 1, fg = 'blue4', bg = 'steelblue1', font = self.ButtonFont, command = self.SubmitFun)
        self.Submit.place(x = 70, y = 580)
        self.Back = Button(self.frame, text = "Back", width = 10, height = 1, fg = 'blue4', bg = 'steelblue1', font = self.ButtonFont, command = Backfun)
        self.Back.place(x = 350, y = 580)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()

        self.CombinedMaths = Checkbutton(self.frame, text = "Combined Mathematics", font = self.LableFont, bg = 'LightBlue2', onvalue = 1, offvalue = 0, variable = self.var1)
        self.CombinedMaths.place (x =80, y = 450)
        self.IT = Checkbutton(self.frame, text = "Information Technology", font = self.LableFont , bg = 'LightBlue2', onvalue = 1, offvalue = 0, variable = self.var2)
        self.IT.place (x =80, y = 490)
        self.Physics = Checkbutton(self.frame, text = "Physics", font = self.LableFont , bg = 'LightBlue2', onvalue = 1, offvalue = 0, variable = self.var3)
        self.Physics.place (x =80, y = 530)
        self.Chemistry = Checkbutton(self.frame, text = "Chemistry", font = self.LableFont , bg = 'LightBlue2', onvalue = 1, offvalue = 0, variable = self.var4)
        self.Chemistry.place (x =380, y = 450)
        self.Biology = Checkbutton(self.frame, text = "Biology", font = self.LableFont , bg = 'LightBlue2', onvalue = 1, offvalue = 0, variable = self.var5)
        self.Biology.place (x =380, y = 490)
        self.English = Checkbutton(self.frame, text = "English", font = self.LableFont , bg = 'LightBlue2', onvalue = 1, offvalue = 0, variable = self.var6)
        self.English.place (x =380, y = 530)

    def SubmitFun(self):

        com_maths = 0
        it = 0
        physics = 0
        chemistry = 0
        biology = 0
        english = 0

        if self.var1.get() == 1:
            com_maths = 1
        if self.var2.get() == 1:
            it = 1
        if self.var3.get() == 1:
            physics = 1
        if self.var4.get() == 1:
            chemistry = 1
        if self.var5.get() == 1:
            biology = 1
        if self.var6.get() == 1:
            english = 1

        stu_insert_query = "INSERT INTO student(stu_name, stu_address, stu_contact, stu_grade, com_maths, it, physics, chemistry, biology,english) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        student = (self.FullNameEnter.get(), self.AddressEnter.get(), self.ContactNumberEnter.get(), self.clicked.get(), com_maths, it, physics, chemistry, biology, english)

        cursor.execute(stu_insert_query, student)
        connector.commit()

        cursor.execute("SELECT stu_id FROM student WHERE (SELECT MAX(stu_id) FROM student)")
        result = cursor.fetchall()
        for i in result:
            ID = i[0]
        messagebox.showinfo("Register Successful !","Hello "+ self.FullNameEnter.get()+" ! \nYou have registered our institute successfully.\nYour Student ID is" + str(ID) + ". \nPlease keep Remember it.")
        self.clearFun()

    def clearFun(self):
        self.FullNameEnter.delete(0, END)
        self.AddressEnter.delete(0, END)
        self.ContactNumberEnter.delete(0, END)
        self.clicked.set("Primary Classes")

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

def Backfun():
    StudentForm.destroy()
    import Admin_Activities_GUI

StudentForm = Tk()
InsertStudent = StudentInformationGUI(StudentForm) 
StudentForm.mainloop()
