from tkinter import * 
import customtkinter 
from config.constants import EMPLOYEE_REGISTER_TITLE

class EmployeeRegComponent: 

    def __init__(self): 
        self.registerStudentWindow = customtkinter.CTk()
        self.registerStudentWindow.geometry("800x700")
        self.registerStudentWindow.resizable(False, False)
        self.registerStudentWindow.title(EMPLOYEE_REGISTER_TITLE)
        self.registerStudentLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Employee Registration", font = customtkinter.CTkFont(size = 30))
        self.registerStudentLabel.place(relx = 0.32, rely = 0.1)

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
        self.usernameLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = 'UserName', font = customtkinter.CTkFont(size = 17))
        self.usernameEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width = 200)
        self.usernameLabel.place(relx = 0.2, rely = 0.3)
        self.usernameEntry.place(relx = 0.2, rely = 0.35)

        ### Email Address 
        self.userEmailLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Email Address", font = customtkinter.CTkFont(size = 17))
        self.userEmailEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width = 200)
        self.userEmailLabel.place(relx = 0.6, rely = 0.3)
        self.userEmailEntry.place(relx = 0.6, rely = 0.35)

        ### password and confirm password. 
        self.userPasswordLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Password", font = customtkinter.CTkFont(size = 17))
        self.userPasswordEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width = 200)
        self.userPasswordLabel.place(relx = 0.2, rely = 0.4)
        self.userPasswordEntry.place(relx = 0.2, rely = 0.45)

        ### confirm password 
        self.userConfirmPasswordLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Confirm Password", font = customtkinter.CTkFont(size = 17))
        self.userConfirmPasswordEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width = 200)
        self.userConfirmPasswordLabel.place(relx = 0.6, rely = 0.4)
        self.userConfirmPasswordEntry.place(relx = 0.6, rely = 0.45)

        ### phone number
        self.userPhoneNumberLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Phone", font = customtkinter.CTkFont(size = 17))
        self.userPhoneNumberEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font = customtkinter.CTkFont(size = 17), width = 200)
        self.userPhoneNumberLabel.place(relx = 0.2, rely = 0.5)
        self.userPhoneNumberEntry.place(relx = 0.2, rely = 0.55)

        ### interval 
        self.intervalTimeSetLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = "Report Interval Time", font = customtkinter.CTkFont(size = 17))
        self.intervalTimeSetLabel.place(relx = 0.6, rely = 0.5)
        self.intervalTimeSetEntry = customtkinter.CTkEntry(master = self.registerStudentWindow, font= customtkinter.CTkFont(size = 17))
        self.intervalTimeSetEntry.place(relx = 0.6, rely = 0.55)
        self.timeLabel = customtkinter.CTkLabel(master = self.registerStudentWindow, text = 'Hours', font = customtkinter.CTkFont(size = 15))
        self.timeLabel.place(relx = 0.79, rely = 0.55)
        self.userRegistrationBtn = customtkinter.CTkButton(master = self.registerStudentWindow, text = "Register Employee", command = self.registerStudent, width=200) 
        self.userRegistrationBtn.place(relx = 0.35, rely = 0.64)

    def render(self): 
        self.registerStudentWindow.mainloop()

    def registerStudent(self):
        error_msg = ""
        student_details = {}
        student_details['first_name'] = self.firstnameEntry.get()
        student_details['last_name'] = self.lastnameEntry.get()
        student_details['email'] = self.userEmailEntry.get()
        student_details['password'] = self.userPasswordEntry.get()
        student_details['phone'] = self.userPhoneNumberEntry.get()
        student_details['interval'] = self.userConfirmPasswordEntry.get()
        student_details['user_name'] = self.usernameEntry.get()
        print(student_details)
        for i, j in student_details.items(): 
            if len(j) == 0:
                error_msg = " ".join(i.split("_"))  + " Can\'t be Empty !!!"
                break
        if error_msg != "":
            error_msg = error_msg.capitalize()
            alert_root = customtkinter.CTk()
            alert_root.geometry("400x150")
            alert_root.title("Alert Box")
            alert_root.resizable(False, False)
            error_message_label = customtkinter.CTkLabel(master=alert_root, text = error_msg, font = customtkinter.CTkFont(size = 17))
            error_message_label.place(relx = .3, rely = .1)
            cancel_btn = customtkinter.CTkButton(master = alert_root, text = "OK", command= lambda : alert_root.destroy())
            cancel_btn.place(relx = 0.35, rely = .4)
            alert_root.mainloop()
        else: 
            pass 


        
        