from tkinter import * 
import customtkinter 
from config.constants import DASHBOARD_TITLE
from config.url_resources import BACKEND_BASE_URL, STRESS_BLINK_DETECTOR, SRESS_BLINK_DATA_GET
import os
import threading
import numpy as np
import requests 

## graph plotting things. 
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

class DashBoardComponent: 

    def __init__(self, access_token : str = ""):
        print("#" * 10 + " " + access_token + " " + "#"* 10)
        print("#" * 20)
        self.access_token = access_token 
        self.activateFlag = False
        self.dashboardWindow = customtkinter.CTk()
        self.dashboardWindow.geometry("1200x700")
        self.dashboardWindow.title(DASHBOARD_TITLE)
        self.dashboardWindow.grid_rowconfigure(0, weight=1)
        self.dashboardWindow.grid_columnconfigure(1, weight=1)
        self.navigationFrame = customtkinter.CTkFrame(self.dashboardWindow, corner_radius=0, bg_color=("gray", "gray"))
        self.navigationFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.navigationFrame.grid_rowconfigure(10, weight=1)
        self.activate_btn = customtkinter.CTkButton(self.navigationFrame, text="Activate", compound="left", 
                        font=customtkinter.CTkFont(size=15, weight="bold"),fg_color='green', 
                        command=self.activate)
        self.activate_btn.grid(row=0, column=0, pady=30, padx = 30)
        ### btn list 
        self.alert_tile = customtkinter.CTkButton(self.navigationFrame, text = "Alerts", fg_color='transparent',font=customtkinter.CTkFont(size = 15),
                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), height=40, border_spacing=10,corner_radius=0, command=self.select_alert_tile)
        self.alert_tile.grid(row = 1, column = 0, sticky = 'ew', pady = 10)
        
        self.stress_tile = customtkinter.CTkButton(self.navigationFrame, text = "Blink Rate", fg_color='transparent', font = customtkinter.CTkFont(size = 15),
                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), height=40, border_spacing=10,width=200, corner_radius=0, command=self.select_stress_tile )
        self.stress_tile.grid(row = 2, column = 0, sticky = 'ew', pady = 10)

        self.step_count = customtkinter.CTkButton(self.navigationFrame, text = "Step Count", fg_color='transparent', font = customtkinter.CTkFont(size = 15),
                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), height=40, border_spacing=10,width=200,  corner_radius=0, command=self.select_step_count_tile)
        self.step_count.grid(row = 3, column = 0, sticky = 'ew', pady = 10)
        self.browsing_classification = customtkinter.CTkButton(self.navigationFrame, text = "Browing Pattern", fg_color='transparent', font = customtkinter.CTkFont(size = 15),
                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), height=40, border_spacing=10,width=200,  corner_radius=0, command=self.select_browsing_title)
        self.browsing_classification.grid(row = 4, column = 0, sticky = 'ew', pady = 10)

        ### alert frame 
        self.alert_frame = customtkinter.CTkFrame(master = self.dashboardWindow)
        self.alert_label = customtkinter.CTkLabel(master = self.alert_frame, text = 'Alert Tab', font = customtkinter.CTkFont(size = 30))
        self.alert_label.place(relx = 0.05, rely = 0.1)
        self.stress_frame = customtkinter.CTkFrame(master = self.dashboardWindow)
        self.stress_frame_label = customtkinter.CTkLabel(master = self.stress_frame, text = 'Blink and Stress Level Tab', font = customtkinter.CTkFont(size = 30))
        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot()
        # line, = ax.hist()
        res = requests.post(BACKEND_BASE_URL + SRESS_BLINK_DATA_GET, json = {
            "access_token": self.access_token
        })
        data = res.json()
        print(data)
        ax.set_xlabel("timestamp")
        ax.set_ylabel("stress level")
        canvas = FigureCanvasTkAgg(fig, master=self.stress_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x = 70, y = 150, width=700)
        self.stress_frame_label.place(relx = 0.05, rely = 0.1)
        self.step_count_frame = customtkinter.CTkFrame(master = self.dashboardWindow)
        self.step_count_frame_label = customtkinter.CTkLabel(master = self.step_count_frame, text = "Step Count Tab", font = customtkinter.CTkFont(size = 30))
        self.step_count_frame_label.place(relx = 0.05, rely = 0.1)
        self.browsing_frame = customtkinter.CTkFrame(master = self.dashboardWindow)
        self.browsing_frame_label = customtkinter.CTkLabel(master = self.browsing_frame, text = "Browing Pattern Tab", font = customtkinter.CTkFont(size = 30))
        self.browsing_frame_label.place(relx = 0.05, rely = 0.1)
        self.select_by_name("alert")

    def render(self): 
        self.dashboardWindow.mainloop()

    def activate(self): 
        if self.activateFlag:
            self.activateFlag = False 
            self.activate_btn.configure(text = "Activate")
            self.activate_btn.configure(fg_color = 'green')
        else:
            self.activateFlag = True 
            thread = threading.Thread(target=os.system("python3 " + STRESS_BLINK_DETECTOR + " --access-token " + f"{self.access_token}"))
            thread.start()
            self.activate_btn.configure(text = "DeActivate")
            self.activate_btn.configure(fg_color = 'red')
        

    def select_by_name(self, name : str): 
        self.alert_tile.configure(fg_color = ("gray75", "gray25") if name == "alert" else "transparent")
        self.stress_tile.configure(fg_color = ("gray75", "gray25") if name == "stress" else "transparent")
        self.step_count.configure(fg_color = ("gray75", "gray25") if name == "step_count" else "transparent")
        self.browsing_classification.configure(fg_color = ("gray75", "gray25") if name == "browsing" else "transparent")
        if name == "alert":
            self.alert_frame.grid(row = 0, column = 1, sticky = 'nsew')
        else: 
            self.alert_frame.grid_forget()
        if name == "stress":
            self.stress_frame.grid(row = 0, column = 1, sticky = 'nsew')
        else:
            self.stress_frame.grid_forget()
        
        if name == "step_count":
            self.step_count_frame.grid(row = 0, column = 1, sticky = 'nsew')
        else:
            self.step_count_frame.grid_forget()
        
        if name == "browsing":
            self.browsing_frame.grid(row = 0, column = 1, sticky = 'nsew')
        else:
            self.browsing_frame.grid_forget()

    
    def select_alert_tile(self):
        self.select_by_name("alert")

    def select_stress_tile(self):
        self.select_by_name("stress")

    def select_step_count_tile(self):
        self.select_by_name("step_count")

    def select_browsing_title(self): 
        self.select_by_name("browsing")