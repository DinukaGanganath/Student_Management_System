import os
from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, PhotoImage, Frame, Radiobutton, IntVar, END
import tkinter as tk
import tkinter.font as font
from cryptography.fernet import Fernet
import mysql.connector

connector = mysql.connector.connect(host = "localhost", user = "root", passwd ="root", database="student_management_system")
cursor = connector.cursor()

class SignUpGUI:

    def __init__(self, SignUp):
        self.SignUp = SignUp
        self.SignUp.geometry("1100x650")
        self.SignUp.title("Sign Up")

        self.TitleFont = font.Font(family = 'Helvetica', size = 45, weight= 'bold' )
        self.LableFont = font.Font(family = 'Helvetica', size = 20)
        self.SubTitleFont = font.Font(family = 'Helvetica', size = 20, weight ='bold')
        self.ButtonFont = font.Font(family = 'Helvetica', size = 20, weight = 'bold')

        self.bg = tk.PhotoImage(file = "Images/class room.png")
        self.Picture = tk.Label(self.SignUp, image = self.bg)
        self.Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

        self.frame = tk.Frame(self.SignUp, width = 840, height = 500, bg = 'bisque')
        self.frame.place(x = 100, y = 75)

        self.title = tk.Label(self.frame, text = "Sign Up", fg = 'coral4', bg = 'bisque', font = self.TitleFont, anchor = 'center')
        self.title.place(x= 315, y = 10)

        self.yourId = tk.Label(self.frame, text = "ID Number", font = self.SubTitleFont,  bg = 'bisque')
        self.yourId.place(x = 50, y = 100)
        self.password = tk.Label(self.frame, text = "Enter Password", font = self.SubTitleFont,  bg = 'bisque')
        self.password.place(x = 50, y = 225)
        self.Repassword = tk.Label(self.frame, text = "Confirm Password", font = self.SubTitleFont,  bg = 'bisque')
        self.Repassword.place(x = 50, y = 350)
        self.yourId = tk.Label(self.frame, text = "Select Character", font = self.SubTitleFont,  bg = 'bisque')
        self.yourId.place(x = 600, y = 110)

        self.IdEnter = tk.Entry(self.frame, font = self.LableFont, width = 30)
        self.IdEnter.place(x = 70, y = 150)
        self.PWEnter = tk.Entry(self.frame, font = self.LableFont, width = 30)
        self.PWEnter.place(x = 70, y = 280)
        self.RePWEnter = tk.Entry(self.frame, font = self.LableFont, width = 30)
        self.RePWEnter.place(x = 70, y = 410)

        self.SignUpButton = tk.Button(self.frame, text = "Sign Up", width = 10, height = 1, fg = 'red4', bg = 'navajo white', font = self.ButtonFont, command = self.savePassword)
        self.SignUpButton.place(x = 630, y = 370)

        self.var = tk.IntVar()

        self.LectureLogin = tk.Radiobutton(self.frame, text = "Lecture Log In", font = self.LableFont , bg = 'bisque', value = 1, variable = self.var)
        self.LectureLogin.place (x =600, y = 160)
        self.StudentsLogin = tk.Radiobutton(self.frame, text = "Student Log In", font = self.LableFont , bg = 'bisque', value = 2, variable = self.var)
        self.StudentsLogin.place (x =600, y = 230)

    def passwordValidate(self):

        password = self.PWEnter.get()

        numbers = upperChar = character = length = False

        if len(password) >= 8:
            length = True

        for letter in password:
            if letter.isascii() and (not letter.isalnum()):
                character = True
            if letter.isupper():
                upperChar = True
            if letter.isnumeric():
                numbers = True

        if character and upperChar and numbers and length:
            return True
        else:
            tk.messagebox.showwarning("Invalid Password", "Create your password using at least one character, one number and uppercase letter.")
            self.clearFun()
            return False

    def savePassword(self):

        password = self.PWEnter.get()
        repassword = self.RePWEnter.get()

        id = int(self.IdEnter.get())
        std_pw_query = "UPDATE student SET password = %s WHERE stu_id = %s"
        lec_pw_query = "UPDATE lecturer SET password = %s WHERE lecturer_id = %s"

        if not (self.var.get() == 1 or self.var.get() == 2):
            tk.messagebox.showwarning("Less information", "Please select your role.")
            self.clearFun()
        elif not (password == repassword):
            tk.messagebox.showwarning("Incorrect input", "Confirmation password is not match with the password.")
            self.clearFun()

        if self.checkAvailability():
            if self.var.get()==1 and self.passwordValidate():
                cursor.execute(lec_pw_query, (self.passwordEncrypt(), id))
                tk.messagebox.showinfo("Password Saved", "Your password saved successfully !")
                GoLogInPage()
            elif self.var.get()==2 and self.passwordValidate():
                cursor.execute(std_pw_query, (self.passwordEncrypt(), id))
                tk.messagebox.showinfo("Password Saved", "Your password saved successfully !")
                GoLogInPage()

        connector.commit()

    def passwordEncrypt(self):

        if not os.path.isfile('key.key'):
            myKey = Fernet.generate_key()
            file = open('key.key', 'wb')
            file.write(myKey)
            file.close()

        file = open('key.key', 'rb')
        key = file.read()
        file.close()

        message = self.PWEnter.get()
        encoded = message.encode()

        f = Fernet(key)
        encrypted = f.encrypt(encoded)

        return encrypted

    def checkAvailability(self):

        stu_password_query = "SELECT * FROM student WHERE stu_id = {}"
        lec_password_query = "SELECT * FROM lecturer WHERE lecturer_id = {}"

        if self.var.get() == 1:
            cursor.execute(lec_password_query.format(int(self.IdEnter.get())))
        if self.var.get() == 2:
            cursor.execute(stu_password_query.format(int(self.IdEnter.get())))

        results = cursor.fetchall()
        if len(results) == 0:
            tk.messagebox.showwarning("Wrong input", "The id you input is wrong.")
            self.clearFun()
            return False
        else:
            for r in results:
                print(r)
                if not (str(r[11]) == "None"):
                    tk.messagebox.showwarning("Can not make password", "This account already has a password")
                    self.clearFun()
                    return False
                else:
                    return True

    def clearFun(self):
        self.IdEnter.delete(0, END)
        self.PWEnter.delete(0, END)
        self.RePWEnter.delete(0, END)
        self.var.set(0)

def GoLogInPage():
    SignUp.destroy()
    import Log_In_GUI

SignUp = tk.Tk()
signup = SignUpGUI(SignUp)
SignUp.mainloop()