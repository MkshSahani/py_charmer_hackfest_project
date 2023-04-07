from tkinter import * 
import customtkinter 
from config.constants import STUDENT_REG_TITLE

class StudentRegistrationComponent: 

    def __init__(self): 
        self.registerStudentWindow = customtkinter.CTk()
        self.registerStudentWindow.geometry("800x700")
        self.registerStudentWindow.resizable(False, False)
        self.registerStudentWindow.title(STUDENT_REG_TITLE)
        self.registerStudentLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Student Registration", font = customtkinter.CTkFont(size = 30))
        self.registerStudentLabel.place(relx = 0.3, rely = 0.1)

        ## First Name 
        self.firstnameLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = 'First Name', font = customtkinter.CTkFont(size = 17))
        self.firstnameEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width=200)
        self.firstnameLabel.place(relx = 0.2, rely = 0.2)
        self.firstnameEntry.place(relx = 0.2, rely = 0.25)

        ## Last Name 
        self.lastnameLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = 'Last Name', font = customtkinter.CTkFont(size = 17))
        self.lastnameEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width=200)
        self.lastnameLabel.place(relx = 0.6, rely = 0.2)
        self.lastnameEntry.place(relx = 0.6, rely = 0.25)

        ### UserName 
        self.usernameLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = 'Email Address', font = customtkinter.CTkFont(size = 17))
        self.usernameEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width = 200)
        self.usernameLabel.place(relx = 0.2, rely = 0.3)
        self.usernameEntry.place(relx = 0.2, rely = 0.35)


    def render(self): 
        self.registerStudentWindow.mainloop()

    def registerStudetn(self): 
        pass 