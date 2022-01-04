from tkinter import Tk, Button, StringVar, Entry, Label, OptionMenu, PhotoImage, Frame, Radiobutton, IntVar, END, Spinbox
from tkinter import messagebox
from tkcalendar import DateEntry
import tkinter.font as font
import tkinter as tk
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class AddLectureGUI:
    
    def __init__(self, LectureForm):
        
        self.LectureForm = LectureForm
        LectureForm.geometry("800x700")
        LectureForm.title("Lecture Form")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.SmallButtonFont = font.Font(family = 'Helvetica', size = 10, weight = 'bold')
        
        self.bg = PhotoImage(file = "Images/Student Form.png")
        self.Picture = Label(LectureForm, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(LectureForm, width = 550, height = 650, bg = 'LightBlue2')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Lecture Information", fg = 'Dark Slate Blue', bg = 'LightBlue2', font = self.TitleFont)
        self.title.place(x= 50, y = 10)

        self.SubName = Label(self.frame, text = "Subject :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.SubName.place(x = 10, y = 100)
        self.Lesson = Label(self.frame, text = "Lesson :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Lesson.place(x = 10, y = 180)
        self.Grade = Label(self.frame, text = "Grade :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Grade.place(x = 10, y = 260)
        self.Date = Label(self.frame, text = "Date :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Date.place(x = 10, y =  340)
        self.Time = Label(self.frame, text = "Time :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Time.place(x = 10, y =  420)
        self.Duration = Label(self.frame, text = "Duration :", font = self.SubTitleFont,  bg = 'LightBlue2')
        self.Duration.place(x = 10, y = 500)

        self.sub_clicked = StringVar()
        self.sub_clicked.set("Combined Mathematics")
        self.TSubjectEnter = OptionMenu(self.frame, self.sub_clicked, "Combined Mathematics", "Information Technology", "Physics", "Chemistry", "Biology", "English")
        self.TSubjectEnter.config(font=self.LableFont, width=36)
        self.TSubjectEnter.place(x=80, y=140)
        self.menu = self.frame.nametowidget(self.TSubjectEnter.menuname)
        self.menu.config(font=self.LableFont)

        self.LessonEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.LessonEnter.place(x = 80, y = 220)

        self.clicked = StringVar()
        self.clicked.set("Primary Classes")
        self.GradeEnter = OptionMenu(self.frame, self.clicked, "Primary Classes", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Ordinary Level", "Advanced Level", "Adult Classes")
        self.GradeEnter.config(font=self.LableFont, width=36)
        self.GradeEnter.place(x=80, y=300)
        self.menu = self.frame.nametowidget(self.GradeEnter.menuname)
        self.menu.config(font=self.LableFont)

        self.DateEnter = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 40)
        self.DateEnter.place(x = 80, y = 380)
        self.Hour = Spinbox(self.frame, from_=00, to=23, format="%02.0f",font = self.LableFont, width = 3)
        self.Hour.place(x = 80, y = 460)
        self.Hour_Min = Label(self.frame, text=" : ", font=self.SubTitleFont, bg='LightBlue2')
        self.Hour_Min.place(x=137, y=460)
        self.Mins = Spinbox(self.frame, from_=00, to=59, format="%02.0f", font = self.LableFont, width = 3)
        self.Mins.place(x=180, y=460)
        self.Min_Sec = Label(self.frame, text=" : ", font=self.SubTitleFont, bg='LightBlue2')
        self.Min_Sec.place(x=237, y=460)
        self.Secs = Spinbox(self.frame, from_=00, to=59, format="%02.0f", font = self.LableFont, width = 3)
        self.Secs.place(x=280, y=460)
        self.DurationEnter = Entry(self.frame, font = self.LableFont, width = 40)
        self.DurationEnter.place(x = 80, y = 540)

        self.Submit = Button(self.frame, text = "Submit", width = 10, height = 1, fg = 'blue4', bg = 'steelblue1', font = self.ButtonFont, command = self.SubmitFun)
        self.Submit.place(x = 70, y = 580)
        self.Submit = Button(self.frame, text = "Back", width = 10, height = 1, fg = 'blue4', bg = 'steelblue1', font = self.ButtonFont, command = BackFun)
        self.Submit.place(x = 350, y = 580)

        self.var = IntVar()

        self.AMValue = Radiobutton(self.frame, text = "AM", font = self.LableFont, bg = 'LightBlue2', value = 1, variable = self.var)
        self.AMValue.place(x = 350, y = 460)
        self.PMValue = Radiobutton(self.frame, text = "PM", font = self.LableFont, bg = 'LightBlue2', value = 2, variable = self.var)
        self.PMValue.place(x = 450, y = 460)

    def SubmitFun(self):

        self.TimeEnter = self.Hour.get() + ":" + self.Mins.get() + ":" + self.Secs.get()

        if self.var.get() == 1:
            Time = 0
        elif self.var.get() == 2:
            Time = 1
        else:
            messagebox.showwarning("Enter value is wrong", "Please Enter the time AM or PM")

        lec_insert_query = "INSERT INTO lec_sessions(lec_subject, lec_lesson, lec_grade, lec_date, lec_time, time_type, duration) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        lecture = (self.sub_clicked.get(), self.LessonEnter.get(), self.clicked.get(), self.DateEnter.get(), self.TimeEnter, Time, self.DurationEnter.get())

        cursor.execute(lec_insert_query, lecture)
        connector.commit()

        cursor.execute("SELECT lec_id FROM lec_sessions WHERE (SELECT MAX(lec_id) FROM student)")
        result = cursor.fetchall()
        for i in result:
            ID = i[0]
        messagebox.showinfo("New Lecture Added !", "You have added a Lecture successfully.\nThe Lecture ID is" + str(ID) + ". \nPlease keep Remember it.")

        self.clear()

    def clear(self):
        self.sub_clicked.set("Combined Mathematics")
        self.LessonEnter.delete(0, END)
        self.DateEnter.delete(0, END)
        self.clicked.set("Primary Classes")
        self.DurationEnter.delete(0, END)
        self.Hour.delete(0, END)
        self.Mins.delete(0, END)
        self.Secs.delete(0, END)

def BackFun():

    LectureForm.destroy()
    from Lecturer_Activities_GUI import LecturerActivitiesGUI
    LecturerActivities = tk.Tk()
    lectureractivities = LecturerActivitiesGUI(LecturerActivities)
    LecturerActivities.mainloop()

LectureForm = Tk()
addlecture = AddLectureGUI(LectureForm) 
LectureForm.mainloop()