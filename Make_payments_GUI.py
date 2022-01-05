from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, StringVar, END, IntVar
import tkinter as tk
from tkcalendar import DateEntry
import tkinter.font as font
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

global months
global indexes

class MakePaymentGUI:
    
    def __init__(self,MakePaymentForm):

        self.MakePaymentForm = MakePaymentForm
        MakePaymentForm.geometry("800x700")
        MakePaymentForm.title("Make Payment")

        self.TitleFont = font.Font(family = 'Helvetica', size = 35, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 15)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 15, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
        self.smallFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
        self.smallButtonFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')

        self.bg = PhotoImage(file = "Images//Edit Student.png")
        self.Picture = Label(MakePaymentForm, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = Frame(MakePaymentForm, width = 550, height = 650, bg = 'antique white')
        self.frame.place(x = 100, y = 30)

        self.title = Label(self.frame, text = "Make Payment", fg = 'indian red', bg = 'antique white', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 90, y = 10)

        self.EnterID = Label(self.frame, text = "Enter ID : ", font = self.smallFont, bg = 'antique white')
        self.EnterID.place(x = 10, y = 83)
        self.FullName = Label(self.frame, text = "Year :", font = self.SubTitleFont,  bg = 'antique white')
        self.FullName.place(x = 10, y = 150)
        self.FullName = Label(self.frame, text = "Month and Date :", font = self.SubTitleFont,  bg = 'antique white')
        self.FullName.place(x = 10, y = 250)
        
        self.IDSearch = Entry(self.frame, font = self.LableFont, width = 27)
        self.IDSearch.place(x = 100, y = 83)
        self.january = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.january.place(x = 120, y = 300)
        self.february = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.february.place(x = 120, y = 345)
        self.march = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.march.place(x = 120, y = 390)
        self.april = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.april.place(x = 120, y = 435)
        self.may = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.may.place(x = 120, y = 480)
        self.june = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.june.place(x = 120, y = 525)
        self.july = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.july.place(x = 390, y = 300)
        self.august = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.august.place(x = 390, y = 345)
        self.september = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.september.place(x = 390, y = 390)
        self.october = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.october.place(x = 390, y = 435)
        self.november = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.november.place(x = 390, y = 480)
        self.december = DateEntry(self.frame, selectmode='day', date_pattern = 'yyyy-MM-dd',font = self.LableFont, width = 10)
        self.december.place(x = 390, y = 525)

        self.january.delete(0, END)
        self.february.delete(0, END)
        self.march.delete(0, END)
        self.april.delete(0, END)
        self.may.delete(0, END)
        self.june.delete(0, END)
        self.july.delete(0, END)
        self.august.delete(0, END)
        self.september.delete(0, END)
        self.october.delete(0, END)
        self.november.delete(0, END)
        self.december.delete(0, END)

        self.Search = Button(self.frame, text = "Search", width = 10, fg = 'red', bg = 'antique white', font = self.smallButtonFont, command = self.Searchfun)
        self.Search.place(x = 415, y = 80)
        self.Edit = Button(self.frame, text = "Edit", width = 10, height = 1, fg = 'red', bg = 'rosybrown1', font = self.ButtonFont, command = self.EditFun)
        self.Edit.place(x = 70, y = 580)
        self.Back = Button(self.frame, text = "Back", width = 10, height = 1, fg = 'red', bg = 'rosybrown1', font = self.ButtonFont, command = Backfun)
        self.Back.place(x = 350, y = 580)

        self.var = IntVar()

        self.Y2019 = Radiobutton(self.frame, text = "2019", font = self.LableFont, bg = 'antique white', value = 2019, variable = self.var)
        self.Y2019.place (x = 40, y = 190)
        self.Y2020 = Radiobutton(self.frame, text = "2020", font = self.LableFont , bg = 'antique white', value = 2020, variable = self.var)
        self.Y2020.place (x = 140, y = 190)
        self.Y2021 = Radiobutton(self.frame, text = "2021", font = self.LableFont , bg = 'antique white', value = 2021, variable = self.var)
        self.Y2021.place (x = 240, y = 190)
        self.Y2022 = Radiobutton(self.frame, text = "2022", font = self.LableFont , bg = 'antique white', value = 2022, variable = self.var)
        self.Y2022.place (x = 340, y = 190)
        self.Y2023 = Radiobutton(self.frame, text = "2023", font = self.LableFont , bg = 'antique white', value = 2023, variable = self.var)
        self.Y2023.place (x = 440, y = 190)

        self.Month1 = IntVar()
        self.Month2 = IntVar()
        self.Month3 = IntVar()
        self.Month4 = IntVar()
        self.Month5 = IntVar()
        self.Month6 = IntVar()
        self.Month7 = IntVar()
        self.Month8 = IntVar()
        self.Month9 = IntVar()
        self.Month10 = IntVar()
        self.Month11 = IntVar()
        self.Month12 = IntVar()

        self.Januarylbl = Label(self.frame, text="January", font=self.LableFont, bg='antique white')
        self.Januarylbl.place (x =20, y = 300)
        self.Februarylbl = Label(self.frame, text="February", font=self.LableFont, bg='antique white')
        self.Februarylbl.place (x =20, y = 345)
        self.Marchlbl = Label(self.frame, text="March", font=self.LableFont, bg='antique white')
        self.Marchlbl.place (x =20, y = 390)
        self.Aprillbl = Label(self.frame, text="April", font=self.LableFont, bg='antique white')
        self.Aprillbl.place (x =20, y = 435)
        self.Maylbl = Label(self.frame, text="May", font=self.LableFont, bg='antique white')
        self.Maylbl.place (x =20, y = 480)
        self.Junelbl = Label(self.frame, text="June", font=self.LableFont, bg='antique white')
        self.Junelbl.place (x =20, y = 525)
        self.Julylbl = Label(self.frame, text="July", font=self.LableFont, bg='antique white')
        self.Julylbl.place (x =270, y = 300)
        self.Augustlbl = Label(self.frame, text="August", font=self.LableFont, bg='antique white')
        self.Augustlbl.place (x =270, y = 345)
        self.Septemberlbl = Label(self.frame, text="September", font=self.LableFont, bg='antique white')
        self.Septemberlbl.place (x =270, y = 390)
        self.Octoberlbl = Label(self.frame, text="October", font=self.LableFont, bg='antique white')
        self.Octoberlbl.place (x =270, y = 435)
        self.Novemberlbl = Label(self.frame, text="November", font=self.LableFont, bg='antique white')
        self.Novemberlbl.place (x =270, y = 480)
        self.Decemberlbl = Label(self.frame, text="December", font=self.LableFont, bg='antique white')
        self.Decemberlbl.place (x =270, y = 525)

    def Searchfun(self):

        try:
            stu_id = int(self.IDSearch.get())
            months = [self.january, self.february, self.march, self.april, self.may, self.june, self.july, self.august, self.september, self.october, self.november, self.december]
            indexes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            i = 0
            year = 2000

            if self.var.get() == 2019:
                year = "2019"
            elif self.var.get() == 2020:
                year = "2020"
            elif self.var.get() == 2021:
                year = "2021"
            elif self.var.get() == 2022:
                year = "2022"
            else:
                messagebox.showwarning("Required information !", "Please select the year before enter the information")

            cursor.execute("SELECT * FROM payment_details WHERE stu_id = %s AND year = %s", (stu_id,year))

            results = cursor.fetchall()

            if len(results) == 0 :
                cursor.execute("INSERT INTO payment_details(stu_id, year) VALUES (%s, %s)", (stu_id, year))
                connector.commit()
            else:
                for payment in results:
                    for i in range(len(months)):
                        months[i].set_date(payment[indexes[i]])
                        if str((payment[indexes[i]])) == "None":
                            months[i].delete(0, END)

        except mysql.connector.IntegrityError :
            messagebox.showwarning("Wrong input!", "Entered student id is wrong")

    def EditFun(self):
        months = [self.january, self.february, self.march, self.april, self.may, self.june, self.july, self.august, self.september, self.october, self.november, self.december]
        year = 2000

        if self.var.get() == 2019:
            year = "2019"
        elif self.var.get() == 2020:
            year = "2020"
        elif self.var.get() == 2021:
            year = "2021"
        elif self.var.get() == 2022:
            year = "2022"


        if not months[0].get() == "":
            cursor.execute("UPDATE payment_details SET january = %s WHERE stu_id = %s AND year = %s", (str(months[0].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET january = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[1].get() == "":
            cursor.execute("UPDATE payment_details SET february = %s WHERE stu_id = %s AND year = %s", (str(months[1].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET february = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[2].get() == "":
            cursor.execute("UPDATE payment_details SET march = %s WHERE stu_id = %s AND year = %s", (str(months[2].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET march = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[3].get() == "":
            cursor.execute("UPDATE payment_details SET april = %s WHERE stu_id = %s AND year = %s", (str(months[3].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET april = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[4].get() == "":
            cursor.execute("UPDATE payment_details SET may = %s WHERE stu_id = %s AND year = %s", (str(months[4].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET may = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[5].get() == "":
            cursor.execute("UPDATE payment_details SET june = %s WHERE stu_id = %s AND year = %s", (str(months[5].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET june = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[6].get() == "":
            cursor.execute("UPDATE payment_details SET july = %s WHERE stu_id = %s AND year = %s", (str(months[6].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET july = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[7].get() == "":
            cursor.execute("UPDATE payment_details SET august = %s WHERE stu_id = %s AND year = %s", (str(months[7].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET august = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[8].get() == "":
            cursor.execute("UPDATE payment_details SET september = %s WHERE stu_id = %s AND year = %s", (str(months[8].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET september = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[9].get() == "":
            cursor.execute("UPDATE payment_details SET october = %s WHERE stu_id = %s AND year = %s", (str(months[9].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET october = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[10].get() == "":
            cursor.execute("UPDATE payment_details SET november = %s WHERE stu_id = %s AND year = %s", (str(months[10].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET november = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))

        if not months[11].get() == "":
            cursor.execute("UPDATE payment_details SET december = %s WHERE stu_id = %s AND year = %s", (str(months[11].get()), int(self.IDSearch.get()), year))
        else:
            cursor.execute("UPDATE payment_details SET december = NULL WHERE stu_id = %s AND year = %s",(int(self.IDSearch.get()), year))
        connector.commit()

        self.clearFun()

    def clearFun(self):
        j = 0
        months = [self.january, self.february, self.march, self.april, self.may, self.june, self.july, self.august,self.september, self.october, self.november, self.december]
        self.IDSearch.delete(0, END)
        for j in range(len(months)):
            months[j].delete(0, END)


def Backfun():
    MakePaymentForm.destroy()
    import Admin_Activities_GUI
    #AdminActivities = tk.Tk()
    #adminactivities = AdminActivitiesGUI(AdminActivities)
    #AdminActivities.mainloop()

MakePaymentForm = Tk()
makepaymentform = MakePaymentGUI(MakePaymentForm)
MakePaymentForm.mainloop()