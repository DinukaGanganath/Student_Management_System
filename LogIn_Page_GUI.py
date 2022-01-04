from tkinter import Label, Button, PhotoImage, Tk, Entry, Frame, IntVar, Radiobutton 
import tkinter.font as font

def AdminLogIn():
    password = "12345"
    ID = "admin"
    if (str(IdEnter.get())== ID) & (str(PWEnter.get()) == password):
        print("Log In is Sucsses !")
    else :
        print("No")

LogIn = Tk()

LogIn.geometry("1100x650")
LogIn.title("Log In")

TitleFont = font.Font(family = 'Helvetica', size = 45, weight= 'bold' )
LableFont = font.Font(family = 'Helvetica', size = 20)
SubTitleFont = font.Font(family = 'Helvetica', size = 20, weight ='bold')
ButtonFont = font.Font(family = 'Helvetica', size = 20, weight = 'bold')

bg = PhotoImage(file = "Images/class room.png")
Picture = Label(LogIn, image = bg)
Picture.place(x= 0, y = 0, relwidth = 1, relheight = 1)

frame = Frame(LogIn, width = 840, height = 500, bg = 'bisque')
frame.place(x = 100, y = 75)

title = Label(frame, text = "Log in", fg = 'coral4', bg = 'bisque', font = TitleFont, anchor = 'center')
title.place(x= 325, y = 10)

yourId = Label(frame, text = "ID Number", font = SubTitleFont,  bg = 'bisque')
yourId.place(x = 50, y = 100)
password = Label(frame, text = "Password", font = SubTitleFont,  bg = 'bisque')
password.place(x = 50, y = 225)
SignUp = Label(frame, text = "Haven't Sign Up ? Click here", font = LableFont,  bg = 'bisque')
SignUp.place(x = 100, y =450)
yourId = Label(frame, text = "Select Character", font = SubTitleFont,  bg = 'bisque')
yourId.place(x = 600, y = 100)

IdEnter = Entry(frame, font = LableFont, width = 30)
IdEnter.place(x = 70, y = 150)
PWEnter = Entry(frame, font = LableFont, width = 30)
PWEnter.place(x = 70, y = 280)

Submit = Button(frame, text = "Submit", width = 10, height = 1, fg = 'red4', bg = 'salmon2', font = ButtonFont, command = AdminLogIn)
Submit.place(x = 320, y = 350)
SignUpButton = Button(frame, text = "Sign Up", width = 10, height = 1, fg = 'red4', bg = 'salmon2', font = ButtonFont)
SignUpButton.place(x = 500, y = 440)


var = IntVar()

AdminLogin = Radiobutton(frame, text = "Admin Log In", font = LableFont, bg = 'bisque', value = 1, variable = var)
AdminLogin.place (x =600, y = 150)
LectureLogin = Radiobutton(frame, text = "Lecture Log In", font = LableFont , bg = 'bisque', value = 3, variable = var)
LectureLogin.place (x =600, y = 220)
StudentsLogin = Radiobutton(frame, text = "Student Log In", font = LableFont , bg = 'bisque', value = 2, variable = var)
StudentsLogin.place (x =600, y = 290)



LogIn.mainloop()

