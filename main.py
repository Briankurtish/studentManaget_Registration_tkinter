import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
import sqlite3

root = tb.Window(themename="darkly")
root.title("Student Management + Registration System")

login_student_icon = tk.PhotoImage(file='images/login_student_img.png')
login_admin_icon = tk.PhotoImage(file='images/admin_img.png')
add_student_icon = tk.PhotoImage(file='images/add_student_img.png')
locked_icon = tk.PhotoImage(file='images/locked.png')
unlocked_icon = tk.PhotoImage(file='images/unlocked.png')

# Resize the locked icon
locked_icon_resized = locked_icon.subsample(2, 2)  # Change the subsample values to adjust the size
unlocked_icon_resized = unlocked_icon.subsample(2, 2)  # Change the subsample values to adjust the size


root.geometry("500x600")

def welcome_page():
    
    welcome_page_frame = tb.LabelFrame(root, bootstyle='info')

    heading_label = tb.Label(
        welcome_page_frame,
        text="Welcome to Student Registration and Management System",
        bootstyle="info",
        font=("Helvetica", 14),
        wraplength=300,  # Set the wrap length in pixels
        justify=tk.CENTER,  # Center the text
    )
    heading_label.pack(padx=10, pady=20)


    # Login Button
    student_login_btn = tb.Button(welcome_page_frame, text="Login Student", bootstyle='info')
    student_login_btn.place(x=150, y=125, width=200)

    student_login_img = tb.Label(welcome_page_frame, image=login_student_icon)
    student_login_img.place(x=50, y=100)

    admin_login_btn = tb.Button(welcome_page_frame, text="Login Admin", bootstyle='info')
    admin_login_btn.place(x=150, y=225, width=200)

    admin_login_img = tb.Label(welcome_page_frame, image=login_admin_icon)
    admin_login_img.place(x=50, y=200)

    add_student_btn = tb.Button(welcome_page_frame, text="Login Student", bootstyle='info')
    add_student_btn.place(x=150, y=325, width=200)

    add_student_img = tb.Label(welcome_page_frame, image=add_student_icon)
    add_student_img.place(x=50, y=300)



    welcome_page_frame.pack(pady=30)
    welcome_page_frame.propagate(False)
    welcome_page_frame.configure(width=400, height=420)
    

def student_login_page():
    def show_hide_password(e):
        if password_entry['show'] == '*':
            password_entry.config(show='')
            show_hide_btn.config(image=unlocked_icon_resized)
        else:
            password_entry.config(show='*')
            show_hide_btn.config(image=locked_icon_resized)
        

    student_login_page_frame = tb.LabelFrame(root, bootstyle='info')


    heading_label = tb.Label(
            student_login_page_frame,
            text="Student Login Page",
            bootstyle="info",
            font=("Helvetica", 14),
            wraplength=300,  # Set the wrap length in pixels
            justify=tk.CENTER,  # Center the text
        )
    heading_label.pack(padx=10, pady=10)

    stud_icon_lb = tb.Label(student_login_page_frame, image=login_student_icon)
    stud_icon_lb.place(x=150, y=60)

    id_number_lb = tb.Label(student_login_page_frame, text="Enter Student ID Number", font=("Helvetica", 12))
    id_number_lb.place(x=95, y=160)

    id_number_entry = tb.Entry(student_login_page_frame, font=('Bold', 12), justify=tk.CENTER)
    id_number_entry.place(x=95, y=200)

    password_lb = tb.Label(student_login_page_frame, text="Enter Student Password", font=("Helvetica", 12))
    password_lb.place(x=95, y=250)

    password_entry = tb.Entry(student_login_page_frame, font=('Bold', 12), justify=tk.CENTER, show='*')
    password_entry.place(x=95, y=280)

    show_hide_btn = tb.Label(student_login_page_frame, image=locked_icon_resized)
    show_hide_btn.place(x=300, y=285)
    # Bind the click event to the label
    show_hide_btn.bind("<Button-1>", show_hide_password)


    login_btn = tb.Button(student_login_page_frame, text="Login", bootstyle="info")
    login_btn.place(x=90, y=340, width=200, height=40)

    forgot_password_btn = tb.Button(student_login_page_frame, text="⚠️ Forgot Password", bootstyle="warning-link")
    forgot_password_btn.place(x=120, y=400)


    student_login_page_frame.pack(pady=30)
    student_login_page_frame.propagate(False)
    student_login_page_frame.configure(width=400, height=500)




root.mainloop()