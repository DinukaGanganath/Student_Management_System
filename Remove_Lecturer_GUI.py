from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar, END
import tkinter as tk
import tkinter.font as font
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class RemoveLecturerGUI:

    def __init__(self, RemoveLecturerForm):

        self.RemoveLecturerForm = RemoveLecturerForm
        RemoveLecturerForm.geometry("800x700")
        RemoveLecturerForm.title("Remove the Lecturer")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.smallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
        self.smallButtonFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = PhotoImage(file = "Images//Teacher Edit.png")
        self.Picture = Label(RemoveLecturerForm, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(RemoveLecturerForm, width = 550, height = 650, bg = 'DarkOliveGreen1')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Remove the Lecturer", fg = 'dark green', bg = 'DarkOliveGreen1', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 40, y = 10)

        self.EnterID = Label(self.frame, text = "Enter ID : ", font = self.smallFont, bg = 'DarkOliveGreen1')
        self.EnterID.place(x = 10, y = 70)
        self.FullName = Label(self.frame, text = "Full Name :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.FullName.place(x = 10, y = 100)
        self.Address = Label(self.frame, text = "Address :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.Address.place(x = 10, y = 180)
        self.ContactNumber = Label(self.frame, text = "Contact Number :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.ContactNumber.place(x = 10, y =  260)
        self.Subject = Label(self.frame, text = "Subject :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.Subject.place(x = 10, y =  340)
        self.Grades = Label(self.frame, text = "Grades :", font = self.SubTitleFont,  bg = 'DarkOliveGreen1')
        self.Grades.place(x = 10, y = 420)

        self.IDSearch = Entry(self.frame, font = self.LableFont, width = 27)
        self.IDSearch.place(x = 100, y = 70)
        self.FullNameEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.FullNameEnter.place(x = 80, y = 140)
        self.AddressEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.AddressEnter.place(x = 80, y = 220)
        self.ContactNumberEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.ContactNumberEnter.place(x = 80, y = 300)
        self.SubjectEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.SubjectEnter.place(x = 80, y = 380)

        self.Search = Button(self.frame, text = "Search", width = 10, fg = 'green4', bg = 'DarkOliveGreen1', font = self.smallButtonFont, command = self.Searchfun)
        self.Search.place(x = 415, y = 67)
        self.Edit = Button(self.frame, text = "Remove", width = 10, height = 1, fg = 'green4', bg = 'darkolivegreen3', font = self.ButtonFont, command = self.Removefun)
        self.Edit.place(x = 70, y = 580)
        self.Edit = Button(self.frame, text = "Back", width = 10, height = 1, fg = 'green4', bg = 'darkolivegreen3', font = self.ButtonFont, command = Backfun)
        self.Edit.place(x = 350, y = 580)

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

    def Searchfun(self):

        self.clearFun()

        lecturer_id = int(self.IDSearch.get())
        cursor.execute("SELECT * FROM lecturer WHERE lecturer_id = {}".format(lecturer_id))

        results = cursor.fetchall()

        for lecturer in results:
            self.FullNameEnter.insert(0, lecturer[1])
            self.AddressEnter.insert(0, lecturer[2])
            self.ContactNumberEnter.insert(0, lecturer[3])
            self.SubjectEnter.insert(0, lecturer[4])
            if lecturer[5] == 1:
                self.var1.set(1)
            if lecturer[6] == 1:
                self.var2.set(1)
            if lecturer[7] == 1:
                self.var3.set(1)
            if lecturer[8] == 1:
                self.var4.set(1)
            if lecturer[9] == 1:
                self.var5.set(1)
            if lecturer[10] == 1:
                self.var6.set(1)

    def Removefun(self):

        lecturer_id = int(self.IDSearch.get())
        delete_query = "DELETE FROM lecturer WHERE lecturer_id = {}"
        cursor.execute(delete_query.format(lecturer_id))
        connector.commit()
        messagebox.showinfo("Remove Successful !", "You have removed the lecturers information successfully.")

        self.clearFun()
        self.IDSearch.delete(0, END)

    def clearFun(self):

        self.FullNameEnter.delete(0, END)
        self.AddressEnter.delete(0, END)
        self.ContactNumberEnter.delete(0, END)
        self.SubjectEnter.delete(0, END)

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

def Backfun():
    RemoveLecturerForm.destroy()
    import Admin_Activities_GUI

RemoveLecturerForm = Tk()
editlecturer = RemoveLecturerGUI(RemoveLecturerForm)
RemoveLecturerForm.mainloop()