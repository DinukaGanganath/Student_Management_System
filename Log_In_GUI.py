from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar, END
import tkinter as tk
import tkinter.font as font

from cryptography.fernet import Fernet
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class LogInGUI:

    def __init__(self,LogIn):
        self.LogIn = LogIn
        LogIn.geometry("1100x650")
        LogIn.title("Log In")

        self.TitleFont = font.Font(family = 'Helvetica', size = 45, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 20)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 20, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 20, weight = 'bold')

        self.bg = tk.PhotoImage(file = "Images/class room.png")
        self.Picture = tk.Label(LogIn, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = tk.Frame(LogIn, width = 840, height = 500, bg = 'bisque')
        self.frame.place(x = 100, y = 75)

        self.title = tk.Label(self.frame, text = "Log in", fg = 'coral4', bg = 'bisque', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 325, y = 10)

        self.yourId = tk.Label(self.frame, text = "ID Number", font = self.SubTitleFont,  bg = 'bisque')
        self.yourId.place(x = 50, y = 100)
        self.password = tk.Label(self.frame, text = "Password", font = self.SubTitleFont,  bg = 'bisque')
        self.password.place(x = 50, y = 225)
        self.SignUp = tk.Label(self.frame, text = "Haven't Sign Up ? Click here", font = self.LableFont,  bg = 'bisque')
        self.SignUp.place(x = 100, y =450)
        self.yourId = tk.Label(self.frame, text = "Select Character", font = self.SubTitleFont,  bg = 'bisque')
        self.yourId.place(x = 600, y = 100)

        self.IdEnter = tk.Entry(self.frame, font = self.LableFont, width = 30)
        self.IdEnter.place(x = 70, y = 150)
        self.PWEnter = tk.Entry(self.frame, font = self.LableFont, width = 30)
        self.PWEnter.place(x = 70, y = 280)

        self.Submit = tk.Button(self.frame, text = "Submit", width = 10, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = self.logInFunction)
        self.Submit.place(x = 320, y = 350)
        self.SignUpButton = tk.Button(self.frame, text = "Sign Up", width = 10, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = SignUpSection)
        self.SignUpButton.place(x = 500, y = 440)


        self.var = tk.IntVar()

        self.AdminLogin = tk.Radiobutton(self.frame, text = "Admin Log In", font = self.LableFont, bg = 'bisque', value = 1, variable = self.var)
        self.AdminLogin.place (x =600, y = 150)
        self.LectureLogin = tk.Radiobutton(self.frame, text = "Lecture Log In", font = self.LableFont , bg = 'bisque', value = 3, variable = self.var)
        self.LectureLogin.place (x =600, y = 220)
        self.StudentsLogin = tk.Radiobutton(self.frame, text = "Student Log In", font = self.LableFont , bg = 'bisque', value = 2, variable = self.var)
        self.StudentsLogin.place (x =600, y = 290)

    def decodedPassword(self):

        global decoded
        id = int(self.IdEnter.get())

        if self.var.get() == 2:
            encrypted_password_query = "SELECT * FROM student WHERE stu_id = {}"
            cursor.execute(encrypted_password_query.format(id))

        if self.var.get() == 3:
            encrypted_password_query = "SELECT * FROM lecturer WHERE lecturer_id = {}"
            cursor.execute(encrypted_password_query.format(id))

        results = cursor.fetchall()
        if not (len(results) == 0):
            for r in results:
                decoded = r[11]

            return decoded.encode()
        else:
            return "invalid"

    def getPassword(self):

        if not (self.decodedPassword() == "invalid"):
            file = open('key.key', 'rb')
            key = file.read()
            file.close()

            f = Fernet(key)
            decrypted = f.decrypt(self.decodedPassword())

            original_password = decrypted.decode()
            print(original_password)
            return original_password
        else:
            return "invalid"

    def checkEquality(self):
        if not (self.getPassword() == "invalid"):
            db_password = str(self.getPassword())
            print(db_password)
            print(self.PWEnter.get())
            if db_password == self.PWEnter.get():
                return True
            else:
                messagebox.showwarning("Wrong Information !", "Password you entered is wrong.")
                self.PWEnter.delete(0, END)
                return False
        else:
            messagebox.showwarning("Wrong Information !", "ID Number you entered is wrong.")
            self.clearFun()
            return False

    def logInFunction(self):

        if self.var.get() == 1:
            self.AdminLogIn()

        elif not (self.var.get() == 2 or self.var.get() == 3 or self.var.get() == 1):
            messagebox.showwarning("Attention", "Please select your Role")

        elif self.var.get() == 2 and self.checkEquality():
            messagebox.showinfo("Student Login", "Login Successfully as a student!")
            LogIn.destroy()
            from Student_Activities_GUI import StudentActivitiesGUI
            root = tk.Tk()
            studentactivity = StudentActivitiesGUI(root)
            root.mainloop()

        elif self.var.get() == 3 and self.checkEquality():
            messagebox.showinfo("Lecturer Login", "Login Successfully as a lecturer!")
            LogIn.destroy()
            from Lecturer_Activities_GUI import LecturerActivitiesGUI
            root = tk.Tk()
            lecactivity = LecturerActivitiesGUI(root)
            root.mainloop()
            LogIn.mainloop()

    def AdminLogIn(self):
        password = "12345"
        ID = "admin"
        if (str(self.IdEnter.get())== ID) & (str(self.PWEnter.get()) == password):
            messagebox.showinfo("Admin Login", "Login Successful !")
            
            LogIn.destroy()
            from Admin_Activities_GUI import AdminActivitiesGUI
            AdminActivities = tk.Tk()
            adminactivities = AdminActivitiesGUI(AdminActivities)
            AdminActivities.mainloop()

        else :
            messagebox.showwarning("Wrong Information !", "ID Number and Password you entered is wrong.")
            self.clearFun()

    def clearFun(self):
        self.IdEnter.delete(0, END)
        self.PWEnter.delete(0, END)

def SignUpSection():
    LogIn.destroy()
    from Sign_Up_GUI import SignUpGUI
    root = tk.Tk()
    signup = SignUpGUI(root)
    root.mainloop()

LogIn = tk.Tk()
Login = LogInGUI(LogIn)
LogIn.mainloop()