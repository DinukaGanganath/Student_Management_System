import tkinter
from tkinter import Tk, Button, Entry, Label, PhotoImage, Frame
import tkinter as tk
import tkinter.font as font
import mysql.connector

connector = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student_management_system")
cursor = connector.cursor()


class ViewPaymentsGUI:

    def __init__(self, ViewPayments):

        self.ViewLectures = ViewPayments
        ViewPayments.geometry("800x700")
        ViewPayments.title("View Lecturers")

        self.TitleFont = font.Font(family='Helvetica', size=35, weight='bold')
        self.LableFont = font.Font(family='Helvetica', size=15)
        self.SubTitleFont = font.Font(family='Helvetica', size=15, weight='bold')
        self.ButtonFont = font.Font(family='Helvetica', size=15, weight='bold')
        self.smallFont = font.Font(family='Helvetica', size=12, weight='bold')
        self.smallButtonFont = font.Font(family='Helvetica', size=12, weight='bold')

        self.bg = PhotoImage(file="Images//Teacher Edit.png")
        self.Picture = Label(ViewPayments, image=self.bg)
        self.Picture.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = Frame(ViewPayments, width=550, height=650, bg='DarkOliveGreen1')
        self.frame.place(x=100, y=30)

        self.title = Label(self.frame, text="View Payments", fg='dark green', bg='DarkOliveGreen1', font=self.TitleFont,anchor='center')
        self.title.place(x=90, y=10)

        self.EnterID = Label(self.frame, text="Enter ID : ", font=self.smallFont, bg='DarkOliveGreen1')
        self.EnterID.place(x=10, y=100)
        self.IDSearch = Entry(self.frame, font=self.LableFont, width=27)
        self.IDSearch.place(x=100, y=100)

        self.Year = Label(self.frame, text="year : ", font=self.smallFont, bg='DarkOliveGreen1')
        self.Year.place(x=10, y=150)
        self.YearSearch = tkinter.Spinbox(self.frame, from_=2019, to=2023, font=self.LableFont, width=26)
        self.YearSearch.place(x=100, y=150)

        self.Search = Button(self.frame, text="Search", width=10, fg='green4', bg='DarkOliveGreen1',
                             font=self.smallButtonFont, command=self.Searchfun)
        self.Search.place(x=415, y=120)
        self.Search = Button(self.frame, text="Back", width=10, fg='green4', bg='DarkOliveGreen1', font=self.ButtonFont,
                             command=Backfun)
        self.Search.place(x=200, y=580)

    def Searchfun(self):

        u = 200
        paid=[]
        pay_months = []
        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        stu_id = int(self.IDSearch.get())
        year = self.YearSearch.get()
        stu_search_query = "SELECT * FROM payment_details WHERE stu_id = %s AND year = %s"

        cursor.execute(stu_search_query, (stu_id, year))

        results = cursor.fetchall()
        for payment in results:
            for i in range(len(payment)):
                if i>1:
                   paid.append(payment[i])

        for k in range(len(paid)):
            if str(paid[k]) == "None":
                continue
            else:
                pay_months.append((month[k], str(paid[k])))
        print(pay_months)

        for item in range(len(pay_months)):
            self.mon = Label(self.frame, text=pay_months[item][0], fg='black', bg='DarkOliveGreen1', font=self.LableFont)
            self.mon.place(x=5, y=u)
            self.date = Label(self.frame, text=pay_months[item][1], fg='black', bg='DarkOliveGreen1', font=self.LableFont)
            self.date.place(x=150, y=u)
            u += 50

        query = """SELECT * FROM lec_sessions WHERE lec_grade = %s AND lec_subject = %s"""

def Backfun():
    ViewPaymentsGUI.destroy()
    from Student_Activities_GUI import StudentActivitiesGUI
    StudentActivities = tk.Tk()
    studentactivities = StudentActivitiesGUI(StudentActivities)
    StudentActivities.mainloop()


ViewPaymentForm = Tk()
viewpaymentsform = ViewPaymentsGUI(ViewPaymentForm)
ViewPaymentForm.mainloop()