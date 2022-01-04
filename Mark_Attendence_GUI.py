from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar, END
import tkinter as tk
from uuid import uuid1
import tkinter.font as font
from DataBase import Students, LectureTimeTable

class MarkAttendenceGUI:

    def __init__(self, MarkAttendence):

        self.MarkAttendence = MarkAttendence
        MarkAttendence.geometry("800x700")
        MarkAttendence.title("Mark Attendence")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.smallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
        self.smallButtonFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = PhotoImage(file = "Images//Student Form.png")
        self.Picture = Label(MarkAttendence, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(MarkAttendence, width = 550, height = 650, bg = 'LightBlue2')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Mark Attendence", fg = 'Dark Slate Blue', bg = 'LightBlue2', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 90, y = 10)

        self.EnterID = Label(self.frame, text = "Enter ID : ", font = self.smallFont, bg = 'LightBlue2')
        self.EnterID.place(x = 10, y = 100)
        
        self.IDSearch = Entry(self.frame, font = self.LableFont, width = 27)
        self.IDSearch.place(x = 100, y = 100)
        
        self.Search = Button(self.frame, text = "Search", width = 10, fg = 'blue4', bg = 'LightBlue2', font = self.smallButtonFont, command = self.Searchfun)
        self.Search.place(x = 415, y = 97)
        self.Search = Button(self.frame, text = "Back", width = 10, fg = 'blue4', bg = 'LightBlue2', font = self.ButtonFont, command = Backfun)
        self.Search.place(x = 70, y = 580)
        self.Search = Button(self.frame, text = "Submit", width = 10, fg = 'blue4', bg = 'LightBlue2', font = self.ButtonFont, command = self.SubmitFun)
        self.Search.place(x = 350, y = 580)
        
    def Searchfun(self):

        global LectureTimeTable, AttendStu, AbsentStu
        AttendStu = []
        AbsentStu = []
        u = 150
        self.NoofReg = 0
        self.NoofAt = 0
        self.NoofAb = 0
        for x in LectureTimeTable:
            if x[0] == self.IDSearch.get():
                for i in Students:
                    for j in i[5] :
                        if (x[1] == j) & (x[3] == i[4]):
                            self.Name = str(i[1])
                            self.lec = Label(self.frame, text = self.Name, fg = 'black', bg = 'LightBlue2', font = self.LableFont)
                            self.lec.place(x = 30, y = u)
                            u += 70
                break
            else:
                messagebox.showwarning("Wrong Information!", "Student ID you entered is wrong!")
        
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        
        self.AttendName = Radiobutton(self.frame, text = "Attend", font = self.LableFont, bg = 'LightBlue2', value = 1, variable = self.var1)
        self.AttendName.place(x=280, y = 150)
        self.AbsentName = Radiobutton(self.frame, text = "Absent", font = self.LableFont, bg = 'LightBlue2', value = 2, variable = self.var1)
        self.AbsentName.place(x=430, y = 150)
        self.AttendName = Radiobutton(self.frame, text = "Attend", font = self.LableFont, bg = 'LightBlue2', value = 1, variable = self.var2)
        self.AttendName.place(x=280, y = 220)
        self.AbsentName = Radiobutton(self.frame, text = "Absent", font = self.LableFont, bg = 'LightBlue2', value = 2, variable = self.var2)
        self.AbsentName.place(x=430, y = 220)
        self.AttendName = Radiobutton(self.frame, text = "Attend", font = self.LableFont, bg = 'LightBlue2', value = 1, variable = self.var3)
        self.AttendName.place(x=280, y = 290)
        self.AbsentName = Radiobutton(self.frame, text = "Absent", font = self.LableFont, bg = 'LightBlue2', value = 2, variable = self.var3)
        self.AbsentName.place(x=430, y = 290)
        
        if self.var1.get() == 1:
            AttendStu.append(i[1])
            self.NoofAt += 1
        elif self.var1.get() == 2:
            AbsentStu.append(i[1])
            self.NoofAb += 1
        self.NoofReg += 1

        if self.var2.get() == 1:
            AttendStu.append(i[2])
            self.NoofAt += 1
        elif self.var2.get() == 2:
            AbsentStu.append(i[2])
            self.NoofAb += 1
        self.NoofReg += 1

        if self.var3.get() == 1:
            AttendStu.append(i[3])
            self.NoofAt += 1
        elif self.var3.get() == 2:
            AbsentStu.append(i[3])
            self.NoofAb += 1
        self.NoofReg += 1

        if self.var4.get() == 1:
            AttendStu.append(i[4])
            self.NoofAt += 1
        elif self.var4.get() == 2:
            AbsentStu.append(i[4])
            self.NoofAb += 1
        self.NoofReg += 1

        if self.var5.get() == 1:
            AttendStu.append(i[5])
            self.NoofAt += 1
        elif self.var1.get() == 2:
            AbsentStu.append(i[5])
            self.NoofAb += 1
        self.NoofReg += 1

        if self.var1.get() == 1:
            AttendStu.append(i[1])
            self.NoofAt += 1
        elif self.var1.get() == 2:
            AbsentStu.append(i[1])
            self.NoofAb += 1
        self.NoofReg += 1

        print(self.NoofReg)
        print(self.NoofAb)
        print(self.NoofAt)
        print(AttendStu)
        print(AbsentStu)

    def SubmitFun(self):
        messagebox.showinfo("Submit Successfully", "You have Submit attendence Succesfully")

def Backfun():
    MarkAttendence.destroy()
    from Lecturer_Activities_GUI import LecturerActivitiesGUI
    LecturerActivities = tk.Tk()
    lectureractivities = LecturerActivitiesGUI(LecturerActivities)
    LecturerActivities.mainloop()

MarkAttendence = Tk()
markattendence = MarkAttendenceGUI(MarkAttendence)
MarkAttendence.mainloop()