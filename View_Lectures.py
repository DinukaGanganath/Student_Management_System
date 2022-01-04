from tkinter import Tk, Button, Entry, Label, PhotoImage, Frame
import tkinter as tk
import tkinter.font as font
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class ViewLecturesGUI:

    def __init__(self, ViewLectures):

        self.ViewLectures = ViewLectures
        ViewLectures.geometry("800x700")
        ViewLectures.title("View Lecturers")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.smallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
        self.smallButtonFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = PhotoImage(file = "Images//Teacher Edit.png")
        self.Picture = Label(ViewLectures, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(ViewLectures, width = 550, height = 650, bg = 'DarkOliveGreen1')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "View Lectures", fg = 'dark green', bg = 'DarkOliveGreen1', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 90, y = 10)

        self.EnterID = Label(self.frame, text = "Enter ID : ", font = self.smallFont, bg = 'DarkOliveGreen1')
        self.EnterID.place(x = 10, y = 100)
        
        self.IDSearch = Entry(self.frame, font = self.LableFont, width = 27)
        self.IDSearch.place(x = 100, y = 100)
        
        self.Search = Button(self.frame, text = "Search", width = 10, fg = 'green4', bg = 'DarkOliveGreen1', font = self.smallButtonFont, command = self.Searchfun)
        self.Search.place(x = 415, y = 97)
        self.Search = Button(self.frame, text = "Back", width = 10, fg = 'green4', bg = 'DarkOliveGreen1', font = self.ButtonFont, command = Backfun)
        self.Search.place(x = 200, y = 580)

    def Searchfun(self):

        subjects = []
        u = 150
        stu_id = int(self.IDSearch.get())
        stu_search_query = "SELECT * FROM student WHERE stu_id = {}"

        cursor.execute(stu_search_query.format(stu_id))

        for row in cursor:
            stu_grade = row[4]
            if row[5] == 1: subjects.append("Combined Mathematics")
            if row[6] == 1: subjects.append("Information Technology")
            if row[7] == 1: subjects.append("Physics")
            if row[8] == 1: subjects.append("Chemistry")
            if row[9] == 1: subjects.append("Biology")
            if row[10] == 1: subjects.append("English")

        query = """SELECT * FROM lec_sessions WHERE lec_grade = %s AND lec_subject = %s"""

        for sub in subjects:
            tuple1 = (stu_grade, sub)
            cursor.execute(query, tuple1)
            results = cursor.fetchall()

            for r in results:
                if r[6] == 0:
                    time_type = " AM"
                else:
                    time_type = " PM"
                lec_date = r[4]
                lec_time = r[5]
                lec_lesson = r[2]
                Lec = str("You have " + r[1] + " lecture. On " + str(lec_date) + ". At " + str(lec_time) + time_type + ". \nLesson is " + str(lec_lesson) + "\n")
                self.lec = Label(self.frame, text=Lec, fg='black', bg='DarkOliveGreen1', font=self.LableFont)
                self.lec.place(x=5, y=u)
                u += 70

def Backfun():
    ViewLectures.destroy()
    from Student_Activities_GUI import StudentActivitiesGUI
    StudentActivities = tk.Tk()
    studentactivities = StudentActivitiesGUI(StudentActivities)
    StudentActivities.mainloop()

ViewLectures = Tk()
viewlectures = ViewLecturesGUI(ViewLectures)
ViewLectures.mainloop()