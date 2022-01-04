from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar
import tkinter as tk
import tkinter.font as font
from DataBase import Students, Lecturers
from uuid import uuid1

class AdminActivitiesGUI:

    def __init__(self,AdminActivity):
        self.AdminActivity = AdminActivity
        AdminActivity.geometry("1100x650")
        AdminActivity.title("Admin Activities")

        self.TitleFont = font.Font(family = 'Helvetica', size = 45, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 20)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 20, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 20, weight = 'bold')
        self.SmallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = tk.PhotoImage(file = "Images/ClassRoom.png")
        self.Picture = tk.Label(AdminActivity, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = tk.Frame(AdminActivity, width = 840, height = 500, bg = 'bisque')
        self.frame.place(x = 100, y = 75)

        self.title = tk.Label(self.frame, text = "Admin Activities", fg = 'coral4', bg = 'bisque', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 200, y = 10)

        self.AddLec = tk.Button(self.frame, text = "Add a Lecturer", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = AddLecFun)
        self.AddLec.place(x = 40, y = 100)
        self.AddStu = tk.Button(self.frame, text = "Add a Student", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = AddStuFun)
        self.AddStu.place(x = 450, y = 100)
        self.EditLec = tk.Button(self.frame, text = "Edit a Lecturer", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = EditLecFun)
        self.EditLec.place(x = 40, y = 200)
        self.EditStu = tk.Button(self.frame, text = "Edit a Student", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = EditStuFun)
        self.EditStu.place(x = 450, y = 200)
        self.RemoveLec = tk.Button(self.frame, text = "Remove a Lecturer", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = RemoveLecFun)
        self.RemoveLec.place(x = 40, y = 300)
        self.RemoveStu = tk.Button(self.frame, text = "Remove a Student", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = RemoveStuFun)
        self.RemoveStu.place(x = 450, y = 300)
        self.Payment = tk.Button(self.frame, text = "Mark Payments", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = PaymentsFun)
        self.Payment.place(x = 200, y = 400)
        self.LogOut = tk.Button(self.frame, text = "Log out", width = 7, height = 1, fg = 'red4', bg = 'navajo white', font = self.SmallFont, command = LogOutFun )
        self.LogOut.place(x = 745, y = 15)


def AddLecFun():
    AdminActivities.destroy()
    from Lecturer_Information_GUI import LecturerInformationGUI
    LecturerForm = tk.Tk()
    lecturerinformation = LecturerInformationGUI(LecturerForm)
    LecturerForm.mainloop()

def AddStuFun():
    AdminActivities.destroy()
    from Student_Information_GUI import StudentInformationGUI
    StudentForm = tk.Tk()
    studentinformation = StudentInformationGUI(StudentForm)
    StudentForm.mainloop()

def EditLecFun():
    AdminActivities.destroy()
    from Lecturer_Edit_GUI import EditLecturerGUI
    LecturerEditForm = tk.Tk()
    editlecturer = EditLecturerGUI(LecturerEditForm)
    LecturerEditForm.mainloop()

def EditStuFun():
    AdminActivities.destroy()
    from Student_Edit_GUI import EditStudentGUI
    StudentEditForm = tk.Tk()
    editstudent = EditStudentGUI(StudentEditForm)
    StudentEditForm.mainloop()

def RemoveLecFun():
    AdminActivities.destroy()
    from Remove_Lecturer_GUI import RemoveLecturerGUI
    LecturerRemoveForm = tk.Tk()
    removestudent = RemoveLecturerGUI(LecturerRemoveForm)
    LecturerRemoveForm.mainloop()

def RemoveStuFun():
    AdminActivities.destroy()
    from Remove_Student_GUI import RemoveStudentGUI
    StudentRemoveForm = tk.Tk()
    removestudent = RemoveStudentGUI(StudentRemoveForm)
    StudentRemoveForm.mainloop()

def PaymentsFun():
    AdminActivities.destroy()
    from Make_payments_GUI import MakePaymentGUI
    MakePayment = tk.Tk()
    makepayment = MakePaymentGUI(MakePayment)
    MakePayment.mainloop()

def LogOutFun():
    AdminActivities.destroy()
    from Log_In_GUI import LogInGUI
    LogIn = tk.Tk()
    login = LogInGUI(LogIn)
    LogIn.mainloop()

AdminActivities = tk.Tk()
adminactivities = AdminActivitiesGUI(AdminActivities)
AdminActivities.mainloop()