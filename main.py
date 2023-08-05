import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
import sqlite3

root = tb.Window(themename="darkly")
root.title("Student Management + Registration System")

login_student_icon = tk.PhotoImage(file='images/login_student_img.png')
login_admin_icon = tk.PhotoImage(file='images/admin_img.png')
add_student_icon = tk.PhotoImage(file='images/add_student_img.png')

root.geometry("500x600")

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

root.mainloop()