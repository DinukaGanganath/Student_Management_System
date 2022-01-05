from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, OptionMenu, StringVar, IntVar, END
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class LecturerInformationGUI:

    def __init__(self, LecturerForm):

        self.LecturerForm = LecturerForm
        LecturerForm.geometry("800x700")
        LecturerForm.title("Lecturer Information Form")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.SmallButtonFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = PhotoImage(file = "Images/Teacher.png")
        self.Picture = Label(LecturerForm, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(LecturerForm, width = 550, height = 650, bg = 'DarkOliveGreen1')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Leturer Information", fg = 'dark green', bg = 'DarkOliveGreen1', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 50, y = 10)

        self.TFullName = Label(self.frame, text = "Full Name :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.TFullName.place(x = 10, y = 100)
        self.TAddress = Label(self.frame, text = "Address :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.TAddress.place(x = 10, y = 180)
        self.TContactNumber = Label(self.frame, text = "Contact Number :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.TContactNumber.place(x = 10, y =  260)
        self.TSubject = Label(self.frame, text = "Subject :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.TSubject.place(x = 10, y =  340)
        self.TGrades = Label(self.frame, text = "Grades :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.TGrades.place(x = 10, y = 420)

        self.TFullNameEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.TFullNameEnter.place(x = 80, y = 140)
        self.TAddressEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.TAddressEnter.place(x = 80, y = 220)
        self.TContactNumberEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.TContactNumberEnter.place(x = 80, y = 300)

        self.clicked = StringVar()
        self.clicked.set("Combined Mathematics")
        self.TSubjectEnter = OptionMenu(self.frame, self.clicked, "Combined Mathematics", "Information Technology", "Physics", "Chemistry", "Biology", "English")
        self.TSubjectEnter.config(font=self.LableFont, width=36)
        self.TSubjectEnter.place(x=80, y=380)
        self.menu = self.frame.nametowidget(self.TSubjectEnter.menuname)
        self.menu.config(font=self.LableFont)

        self.Submit = Button(self.frame, text = "Submit", width = 10, height = 1, fg = 'green4', bg = 'darkolivegreen3', font = self.ButtonFont, command = self.Submitfun)
        self.Submit.place(x = 70, y = 580)
        self.Back = Button(self.frame, text = "Back", width = 10, height = 1, fg = 'green4', bg = 'darkolivegreen3', font = self.ButtonFont, command = Backfun)
        self.Back.place(x = 350, y = 580)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()

        self.Primary = Checkbutton(self.frame, text = "Primary Classes", font = self.LableFont, bg = 'DarkOliveGreen1', onvalue = 1, offvalue = 0, variable = self.var1)
        self.Primary.place (x =80, y = 450)
        self.Grade678 = Checkbutton(self.frame, text = "Grade 6 / 7 / 8", font = self.LableFont , bg = 'DarkOliveGreen1', onvalue = 1, offvalue = 0, variable = self.var2)
        self.Grade678.place (x =80, y = 490)
        self.Grade91011 = Checkbutton(self.frame, text = "Grade 9 / 10 / 11", font = self.LableFont , bg = 'DarkOliveGreen1', onvalue = 1, offvalue = 0, variable = self.var3)
        self.Grade91011.place (x =80, y = 530)
        self.Ordinary = Checkbutton(self.frame, text = "Ordinary Level", font = self.LableFont , bg = 'DarkOliveGreen1', onvalue = 1, offvalue = 0, variable = self.var4)
        self.Ordinary.place (x =350, y = 450)
        self.Advanced = Checkbutton(self.frame, text = "Advanced Level", font = self.LableFont , bg = 'DarkOliveGreen1', onvalue = 1, offvalue = 0, variable = self.var5)
        self.Advanced.place (x =350, y = 490)
        self.Adult = Checkbutton(self.frame, text = "Adult Classes", font = self.LableFont , bg = 'DarkOliveGreen1', onvalue = 1, offvalue = 0, variable = self.var6)
        self.Adult.place (x =350, y = 530)

    def Submitfun(self):
        primary_class = 0
        grade_6_8 = 0
        grade_9_11 = 0
        o_level = 0
        a_level = 0
        adult = 0

        if self.var1.get() == 1:
            primary_class = 1
        if self.var2.get() == 1:
            grade_6_8 = 1
        if self.var3.get() == 1:
            grade_9_11 = 1
        if self.var4.get() == 1:
            o_level = 1
        if self.var5.get() == 1:
            a_level = 1
        if self.var6.get() == 1:
            adult = 1

        lecturer_insert_query = "INSERT INTO lecturer(lecturer_name, lecturer_address, lecturer_contact, lecturer_subject, primary_class, grade_6_8, grade_9_11, o_level, a_level, adult) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        lecturer = (
        self.TFullNameEnter.get(), self.TAddressEnter.get(), self.TContactNumberEnter.get(), self.clicked.get(), primary_class, grade_6_8, grade_9_11, o_level, a_level, adult)

        cursor.execute(lecturer_insert_query, lecturer)
        connector.commit()

        cursor.execute("SELECT lecturer_id FROM lecturer WHERE (SELECT MAX(lecturer_id) FROM lecturer)")
        result = cursor.fetchall()
        for i in result:
            ID = i[0]
    
        messagebox.showinfo("Register Successful !","Hello "+ self.TFullNameEnter.get()+" ! \nYou have registered our institute successfully.\nYour Lecturer ID is " + str(ID) + ". \nPlease keep Remember it.")
        self.clearFun()

    def clearFun(self):
        self.TFullNameEnter.delete(0, END)
        self.TAddressEnter.delete(0, END)
        self.TContactNumberEnter.delete(0, END)
        self.clicked.set("Combined Mathematics")

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

def Backfun():
    LecturerForm.destroy()
    import Admin_Activities_GUI

LecturerForm = Tk()
InsertLecturer = LecturerInformationGUI(LecturerForm) 
LecturerForm.mainloop()
