from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar, END
import tkinter as tk
import tkinter.font as font
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class RemoveStudentGUI:
    
    def __init__(self,RemoveStudentForm):

        self.RemoveStudentForm = RemoveStudentForm
        RemoveStudentForm.geometry("800x700")
        RemoveStudentForm.title("Remove the Student")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.smallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
        self.smallButtonFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = PhotoImage(file = "Images//Edit Student.png")
        self.Picture = Label(RemoveStudentForm, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(RemoveStudentForm, width = 550, height = 650, bg = 'antique white')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Remove the Student", fg = 'indian red', bg = 'antique white', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 40, y = 10)

        self.EnterID = Label(self.frame, text = "Enter ID : ", font = self.smallFont, bg = 'antique white')
        self.EnterID.place(x = 10, y = 70)
        self.FullName = Label(self.frame, text = "Full Name :", font = self.SubTitleFont,  bg = 'antique white')
        self.FullName.place(x = 10, y = 100)
        self.Address = Label(self.frame, text = "Address :", font = self.SubTitleFont,  bg = 'antique white')
        self.Address.place(x = 10, y = 180)
        self.ContactNumber = Label(self.frame, text = "Contact Number :", font = self.SubTitleFont,  bg = 'antique white')
        self.ContactNumber.place(x = 10, y =  260)
        self.Grade = Label(self.frame, text = "Grade :", font = self.SubTitleFont,  bg = 'antique white')
        self.Grade.place(x = 10, y =  340)
        self.Subjects = Label(self.frame, text = "Subjects :", font = self.SubTitleFont,  bg = 'antique white')
        self.Subjects.place(x = 10, y = 420)

        self.IDSearch = Entry(self.frame, font = self.LableFont, width = 27)
        self.IDSearch.place(x = 100, y = 70)
        self.FullNameEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.FullNameEnter.place(x = 80, y = 140)
        self.AddressEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.AddressEnter.place(x = 80, y = 220)
        self.ContactNumberEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.ContactNumberEnter.place(x = 80, y = 300)
        self.GradeEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.GradeEnter.place(x = 80, y = 380)

        self.Search = Button(self.frame, text = "Search", width = 10, fg = 'red', bg = 'antique white', font = self.smallButtonFont, command = self.Searchfun)
        self.Search.place(x = 415, y = 67)
        self.Edit = Button(self.frame, text = "Remove", width = 10, height = 1, fg = 'red', bg = 'rosybrown1', font = self.ButtonFont, command = self.Removefun)
        self.Edit.place(x = 70, y = 580)
        self.Back = Button(self.frame, text = "Back", width = 10, height = 1, fg = 'red', bg = 'rosybrown1', font = self.ButtonFont, command = Backfun)
        self.Back.place(x = 350, y = 580)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()

        self.CombinedMaths = Checkbutton(self.frame, text = "Combined Mathematics", font = self.LableFont, bg = 'antique white', onvalue = 1, offvalue = 0, variable = self.var1)
        self.CombinedMaths.place (x =80, y = 450)
        self.IT = Checkbutton(self.frame, text = "Information Technology", font = self.LableFont , bg = 'antique white', onvalue = 1, offvalue = 0, variable = self.var2)
        self.IT.place (x =80, y = 490)
        self.Physics = Checkbutton(self.frame, text = "Physics", font = self.LableFont , bg = 'antique white', onvalue = 1, offvalue = 0, variable = self.var3)
        self.Physics.place (x =80, y = 530)
        self.Chemistry = Checkbutton(self.frame, text = "Chemistry", font = self.LableFont , bg = 'antique white', onvalue = 1, offvalue = 0, variable = self.var4)
        self.Chemistry.place (x =380, y = 450)
        self.Biology = Checkbutton(self.frame, text = "Biology", font = self.LableFont , bg = 'antique white', onvalue = 1, offvalue = 0, variable = self.var5)
        self.Biology.place (x =380, y = 490)
        self.English = Checkbutton(self.frame, text = "English", font = self.LableFont , bg = 'antique white', onvalue = 1, offvalue = 0, variable = self.var6)
        self.English.place (x =380, y = 530)

    def Removefun(self):

        stu_id = int(self.IDSearch.get())
        delete_query = "DELETE FROM student WHERE stu_id = {}"
        cursor.execute(delete_query.format(stu_id))
        connector.commit()
        messagebox.showinfo("Remove Successful !","You have removed the student information successfully.")

        self.clearFun()
        self.IDSearch.delete(0, END)

    def Searchfun(self):

        self.clearFun()

        stu_id = int(self.IDSearch.get())
        cursor.execute("SELECT * FROM student WHERE stu_id = {}".format(stu_id))

        results = cursor.fetchall()

        for student in results:
            self.FullNameEnter.insert(0, student[1])
            self.AddressEnter.insert(0, student[2])
            self.ContactNumberEnter.insert(0, student[3])
            self.GradeEnter.insert(0, student[4])
            if student[5] == 1:
                self.var1.set(1)
            if student[6] == 1:
                self.var2.set(1)
            if student[7] == 1:
                self.var3.set(1)
            if student[8] == 1:
                self.var4.set(1)
            if student[9] == 1:
                self.var5.set(1)
            if student[10] == 1:
                self.var6.set(1)

    def clearFun(self):

        self.FullNameEnter.delete(0, END)
        self.AddressEnter.delete(0, END)
        self.ContactNumberEnter.delete(0, END)
        self.GradeEnter.delete(0, END)

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

def Backfun():
    RemoveStudentForm.destroy()
    import Admin_Activities_GUI

RemoveStudentForm = Tk()
editstudentform = RemoveStudentGUI(RemoveStudentForm)
RemoveStudentForm.mainloop()