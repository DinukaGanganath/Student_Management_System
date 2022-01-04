from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar
import tkinter as tk
import tkinter.font as font
from DataBase import Students, Lecturers
from uuid import uuid1

class StudentActivitiesGUI:

    def __init__(self,StudentActivity):
        self.StudentActivity = StudentActivity
        StudentActivity.geometry("1100x650")
        StudentActivity.title("Student Activities")

        self.TitleFont = font.Font(family = 'Helvetica', size = 45, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 20)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 20, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 20, weight = 'bold')
        self.SmallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = tk.PhotoImage(file = "Images/ClassRoom.png")
        self.Picture = tk.Label(StudentActivity, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = tk.Frame(StudentActivity, width = 840, height = 500, bg = 'bisque')
        self.frame.place(x = 100, y = 75)

        self.title = tk.Label(self.frame, text = "Student Activities", fg = 'coral4', bg = 'bisque', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 200, y = 10)

        self.ShowLec = tk.Button(self.frame, text = "Show the Lectures", width = 20, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = ShowLecFun)
        self.ShowLec.place(x = 250, y = 250)
        
        
        self.LogOut = tk.Button(self.frame, text = "Log out", width = 7, height = 1, fg = 'red4', bg = 'navajo white', font = self.SmallFont, command = LogOutFun )
        self.LogOut.place(x = 745, y = 15)
        
def ShowLecFun():
    StudentActivities.destroy()
    from View_Lectures import ViewLecturesGUI
    ViewLectures = Tk()
    viewlectures = ViewLecturesGUI(ViewLectures)
    ViewLectures.mainloop()

def LogOutFun():
    StudentActivities.destroy()
    from Log_In_GUI import LogInGUI
    LogIn = tk.Tk()
    logingui = LogInGUI(LogIn)
    LogIn.mainloop()

StudentActivities = tk.Tk()
studentactivities = StudentActivitiesGUI(StudentActivities)
StudentActivities.mainloop()