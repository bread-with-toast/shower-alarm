import tkinter
import customtkinter
import matplotlib.pyplot as plt
import serial
from datetime import datetime
import seaborn as sns

user = ""
passw = ""

root = customtkinter.CTk()
data = serial.Serial("COM4", 9600)

current_time = datetime.now()
timeNow = current_time.strftime("%H:%M")

sns.set_theme()

def log_in():
    if username.get() == user and password.get() == passw:
        msg.config(text="Logged In!", text_color="#46c76a")
        main = customtkinter.CTkToplevel()
        main.geometry("900x400")

        def uptime():
            sns.lineplot(
                x=[1, 2, 3], 
                y=[80, 35, 0.0084],
            ) 
            # 0.0004 = 1 min
            plt.show()

        def time_till():
            while data.inWaiting() == 0:
                pass
            data_packet = str(data.readline(), "utf-8")
            dashboard.config(text=data_packet)

        frame2 = customtkinter.CTkFrame(main)
        frame2.pack(padx=20, pady=20, fill="both", expand=True)

        customtkinter.CTkLabel(frame2, text=f"Greetings, {user}!", text_font=("JetBrains Mono", 24)).pack(pady=20)
        customtkinter.CTkLabel(frame2, text=f"Startup at { timeNow }", text_font=("JetBrains Mono", 10)).pack(pady=20)
        customtkinter.CTkButton(frame2, text="Uptime", command=uptime, text_font=("JetBrains Mono", 10)).pack(pady=20)
        customtkinter.CTkButton(frame2, text="Refresh/Check Information", command=time_till, text_font=("JetBrains Mono", 10)).pack(pady=10)

        dashboard = customtkinter.CTkLabel(frame2, text="", text_font=("JetBrains Mono", 10))
        dashboard.pack(pady=20)

    else:
        msg.config(text="Could Not Log In!", text_color="#fa7383")

frame1 = customtkinter.CTkFrame(root)
frame1.pack(padx=20, pady=20, fill="both", expand=True)

customtkinter.CTkLabel(frame1, text="Shower Alarm Dashboard", text_font=("JetBrains Mono", 24)).pack(pady=20)

username = customtkinter.CTkEntry(frame1, placeholder_text="Username", text_font=("JetBrains Mono", 10))
username.pack(pady=20)

password = customtkinter.CTkEntry(frame1, placeholder_text="Password", text_font=("JetBrains Mono", 10))
password.pack()

customtkinter.CTkButton(frame1, text="Log In", command=log_in, text_font=("JetBrains Mono", 10)).pack(pady=20)
msg = customtkinter.CTkLabel(frame1, text="", text_font=("JetBrains Mono", 10))
msg.pack()

def light():
    customtkinter.set_appearance_mode("light")

def dark():
    customtkinter.set_appearance_mode("dark")

customtkinter.CTkButton(frame1, text="Light Theme", command=light, text_font=("JetBrains Mono", 10)).pack(pady=20)
customtkinter.CTkButton(frame1, text="Dark Theme", command=dark, text_font=("JetBrains Mono", 10)).pack(pady=10)

root.mainloop()