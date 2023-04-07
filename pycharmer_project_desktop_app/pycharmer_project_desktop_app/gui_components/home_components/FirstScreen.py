from tkinter import * 
import customtkinter 
from config.constants import TOPBAR_TITLE
from gui_components.registration_component.student_login_comp import StudentLoginComponent
from gui_components.registration_component.employee_login_comp import EmployeeLoginComponent

class FirstPage: 

    def __init__(self): 
        self.root = customtkinter.CTk()
        self.root.title(TOPBAR_TITLE)
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.textLabel = customtkinter.CTkLabel(master = self.root, text = "Please Choose any one option",
                            font = customtkinter.CTkFont(size = 40, weight="bold"))
        self.textLabel.place(relx = 0.2, rely = 0.3)
        self.studentBtn = customtkinter.CTkButton(master = self.root, text = "Student", height=40, width = 150, command=self.studentBtnCommandAction)
        self.employeeBtn = customtkinter.CTkButton(master = self.root, text = "Employee", height=40, width = 150, command=self.employeeBtnCommandAction) 
        self.studentBtn.place(relx = 0.3, rely = 0.5)
        self.employeeBtn.place(relx  = 0.5, rely = 0.5)
    
    def render(self): 
        self.root.mainloop()

    def studentBtnCommandAction(self): 
        self.root.destroy()
        studentLoginComponent = StudentLoginComponent()
        studentLoginComponent.render()

    def employeeBtnCommandAction(self): 
        self.root.destroy()
        employeeLoginComponent = EmployeeLoginComponent()
        employeeLoginComponent.render()
