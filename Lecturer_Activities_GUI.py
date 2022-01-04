from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar
import tkinter as tk
import tkinter.font as font
from DataBase import Students, Lecturers
from uuid import uuid1

class LecturerActivitiesGUI:

    def __init__(self,LecturerActivity):
        self.LecturerActivity = LecturerActivity
        LecturerActivity.geometry("1100x650")
        LecturerActivity.title("Lecturer Activities")

        self.TitleFont = font.Font(family = 'Helvetica', size = 45, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 20)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 20, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 20, weight = 'bold')
        self.SmallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = tk.PhotoImage(file = "Images//ClassRoom.png")
        self.Picture = tk.Label(LecturerActivity, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = tk.Frame(LecturerActivity, width = 840, height = 500, bg = 'bisque')
        self.frame.place(x = 100, y = 75)

        self.title = tk.Label(self.frame, text = "Lecturer Activities", fg = 'coral4', bg = 'bisque', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 200, y = 10)

        self.AddLec = tk.Button(self.frame, text = "Add a Lecture", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = AddLecFun)
        self.AddLec.place(x = 40, y = 250)
        self.MarkAttendence = tk.Button(self.frame, text = "Mark Attendence", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = MarkAttFun)
        self.MarkAttendence.place(x = 450, y = 250)
        self.LogOut = tk.Button(self.frame, text = "Log out", width = 7, height = 1, fg = 'red4', bg = 'navajo white', font = self.SmallFont, command = LogOutFun )
        self.LogOut.place(x = 745, y = 15)
        
def AddLecFun():
    LecturerActivities.destroy()
    from Add_Lecture_GUI import AddLectureGUI
    LectureForm = tk.Tk()
    addlecture = AddLectureGUI(LectureForm)
    LectureForm.mainloop()

def MarkAttFun():
    LecturerActivities.destroy()
    from Mark_Attendence_GUI import MarkAttendenceGUI
    MarkAttendence = tk.Tk()
    markattendence = MarkAttendenceGUI(MarkAttendence)
    MarkAttendence.mainloop()

def LogOutFun():
    LecturerActivities.destroy()
    from Log_In_GUI import LogInGUI
    LogIn = tk.Tk()
    login = LogInGUI(LogIn)
    LogIn.mainloop()

LecturerActivities = tk.Tk()
lectureractivities = LecturerActivitiesGUI(LecturerActivities)
LecturerActivities.mainloop()