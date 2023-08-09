import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
import sqlite3
import os
import re 
import random

root = tb.Window(themename="darkly")
root.title("Student Management + Registration System")


#Toast messages
fullname_message = ToastNotification(title="Error", 
                          message= "Student Full Name is Required",
                          duration=3000,
                          alert=True,
                          
                          )

age_message = ToastNotification(title="Error", 
                          message= "Student Age is Required",
                          duration=3000,
                          alert=True,
                          
                          )
class_message = ToastNotification(title="Error", 
                          message= "Student Class is Required",
                          duration=3000,
                          alert=True,
                          
                          )

contact_message = ToastNotification(title="Error", 
                          message= "Student Contact Details is Required",
                          duration=3000,
                          alert=True,
                          
                          )

email_message = ToastNotification(title="Error", 
                          message= "Student Email is Required",
                          duration=3000,
                          alert=True,
                          
                          )
valid_email_message = ToastNotification(title="Error", 
                          message= "Enter a Valid Email Address",
                          duration=3000,
                          alert=True,
                          
                          )

password_message = ToastNotification(title="Error", 
                          message= "Student Password is Required",
                          duration=3000,
                          alert=True,
                          
                          )
account_creation = ToastNotification(title="Success", 
                          message= "Student Account Created Successfully",
                          duration=3000,
                          alert=True,
                          
                          )

login_student_icon = tk.PhotoImage(file='images/login_student_img.png')
login_admin_icon = tk.PhotoImage(file='images/admin_img.png')
add_student_icon = tk.PhotoImage(file='images/add_student_img.png')
locked_icon = tk.PhotoImage(file='images/locked.png')
unlocked_icon = tk.PhotoImage(file='images/unlocked.png')

add_student_pic_icon = tk.PhotoImage(file='images/add_image.png')



# Resize the locked icon
locked_icon_resized = locked_icon.subsample(2, 2)  # Change the subsample values to adjust the size
unlocked_icon_resized = unlocked_icon.subsample(2, 2)  # Change the subsample values to adjust the size


root.geometry("500x600")


def init_database():
    if os.path.exists('students_account.db'):
        pass
    else:
        connection = sqlite3.connect('students_account.db')
        
        cursor = connection.cursor()
        
        cursor.execute("""
            
            CREATE TABLE data (
                id_number text,
                password text,
                name text, 
                age text,
                gender text,
                phone_number text,
                class text,
                email text,
                image blob
            )
                        
        """)
        
        connection.commit()
        connection.close()
        
def add_data(id_number, password, name, age, gender, phone_number, student_class, email, pic_data):
    connection = sqlite3.connect('students_account.db')
        
    cursor = connection.cursor()
    
    cursor.execute(f"""
        
        INSERT INTO data VALUES(
            '{id_number}',
            '{password}',
            '{name}', 
            '{age}',
            '{gender}',
            '{phone_number}',
            '{student_class}',
            '{email}',
            ?
        )
                    
    """, [pic_data])
    
    connection.commit()
    connection.close()


def confirmation_box(message):
    
    answer = tk.BooleanVar()
    answer.set(False)
    
    def action(ans):
        answer.set(ans)
        confirmation_box_frame.destroy()
    
    confirmation_box_frame = tb.LabelFrame(bootstyle='primary')
    
    message_lb = tb.Label(confirmation_box_frame, text=message, font=("Helvetica", 11), bootstyle='warning', justify=tk.CENTER,)
    message_lb.pack(pady=30)
    
    cancel_btn = tb.Button(confirmation_box_frame, text='Cancel', bootstyle='danger', command=lambda: action(False))
    cancel_btn.place(x=50, y=150)

    yes_btn = tb.Button(confirmation_box_frame, text='Yes', bootstyle='Success', command=lambda: action(True))
    yes_btn.place(x=200, y=150, width=70)
    
    confirmation_box_frame.place(x=100, y=120, width=320, height=220)
    
    root.wait_window(confirmation_box_frame)
    return answer.get()


def welcome_page():
    
    def forward_to_student_login_page():
        welcome_page_frame.destroy()
        root.update()
        student_login_page()
    
    def forward_to_admin_login_page():
        welcome_page_frame.destroy()
        root.update()
        admin_login_page()
    
    def forward_to_create_account_page():
        welcome_page_frame.destroy()
        root.update()
        add_account_page()
    
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
    student_login_btn = tb.Button(welcome_page_frame, text="Login Student", bootstyle='info', command=forward_to_student_login_page)
    student_login_btn.place(x=150, y=125, width=200)

    student_login_img = tb.Label(welcome_page_frame, image=login_student_icon)
    student_login_img.place(x=50, y=100)

    admin_login_btn = tb.Button(welcome_page_frame, text="Login Admin", bootstyle='info', command=forward_to_admin_login_page)
    admin_login_btn.place(x=150, y=225, width=200)

    admin_login_img = tb.Label(welcome_page_frame, image=login_admin_icon)
    admin_login_img.place(x=50, y=200)

    add_student_btn = tb.Button(welcome_page_frame, text="Create Account", bootstyle='info', command=forward_to_create_account_page)
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
    
    def forward_to_welcome_page(e):
        student_login_page_frame.destroy()
        root.update()
        welcome_page()

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
    
    #Back Button
    back_btn = tb.Label(student_login_page_frame, text='←', bootstyle='danger', font=('Bold', 20))
    back_btn.place(x=10, y=40)
    # Bind the click event to the label
    back_btn.bind("<Button-1>", forward_to_welcome_page)

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


def admin_login_page():
    def show_hide_password(e):
        if password_entry['show'] == '*':
            password_entry.config(show='')
            show_hide_btn.config(image=unlocked_icon_resized)
        else:
            password_entry.config(show='*')
            show_hide_btn.config(image=locked_icon_resized)
            
    def forward_to_welcome_page(e):
        admin_login_page_frame.destroy()
        root.update()
        welcome_page()

    admin_login_page_frame = tb.LabelFrame(root, bootstyle='success')

    heading_label = tb.Label(
                admin_login_page_frame,
                text="Admin Login Page",
                bootstyle="success",
                font=("Helvetica", 14),
                wraplength=300,  # Set the wrap length in pixels
                justify=tk.CENTER,  # Center the text
            )
    heading_label.pack(padx=10, pady=10)
    
    
    
    #Back Button
    back_btn = tb.Label(admin_login_page_frame, text='←', bootstyle='danger', font=('Bold', 20))
    back_btn.place(x=10, y=40)
    # Bind the click event to the label
    back_btn.bind("<Button-1>", forward_to_welcome_page)

    admin_icon_lb = tb.Label(admin_login_page_frame, image=login_admin_icon)
    admin_icon_lb.place(x=150, y=60)

    username_lb = tb.Label(admin_login_page_frame, text="Enter Admin UserName", font=("Helvetica", 12))
    username_lb.place(x=95, y=160)

    username_entry = tb.Entry(admin_login_page_frame, font=('Bold', 12), justify=tk.CENTER)
    username_entry.place(x=95, y=200)

    password_lb = tb.Label(admin_login_page_frame, text="Enter Admin Password", font=("Helvetica", 12))
    password_lb.place(x=95, y=250)

    password_entry = tb.Entry(admin_login_page_frame, font=('Bold', 12), justify=tk.CENTER, show='*')
    password_entry.place(x=95, y=280)

    show_hide_btn = tb.Label(admin_login_page_frame, image=locked_icon_resized)
    show_hide_btn.place(x=300, y=285)
    # Bind the click event to the label
    show_hide_btn.bind("<Button-1>", show_hide_password)

    login_btn = tb.Button(admin_login_page_frame, text="Login", bootstyle="success")
    login_btn.place(x=90, y=340, width=200, height=40)

    forgot_password_btn = tb.Button(admin_login_page_frame, text="⚠️ Forgot Password", bootstyle="warning-link")
    forgot_password_btn.place(x=120, y=400)

    admin_login_page_frame.pack(pady=30)
    admin_login_page_frame.propagate(False)
    admin_login_page_frame.configure(width=400, height=500)

def add_account_page():
    
    #Adding the student picture 
    pic_path = tk.StringVar()
    pic_path.set('')
    
    def open_pic(e):
        path = askopenfilename()
        if path:
            img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
            pic_path.set(path)

            # Add student picture to picture button
            add_pic_btn.config(image=img)
            add_pic_btn.image = img
    

    def forward_to_welcome_page():
        
        ans = confirmation_box(message="Do you want to Leave\nRegistration Form?")
        
        if ans:
            add_account_page_frame.destroy()
            root.update()
            welcome_page()
    

    def check_invalid_email(email):
        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        match = re.match(pattern=pattern , string=email)
        
        return match

    def generate_id_number():
        generated_id = ''
        
        for r in range(6):
            generated_id += str(random.randint(0, 9))
            
            student_id_entry.config(state='normal')
            student_id_entry.delete(0, "end")
            student_id_entry.insert("end", generated_id)
            student_id_entry.config(state='readonly')
            
    
    
    def check_input_validation():
        if student_name_entry.get() == '':
            student_name_entry.config(bootstyle='danger')
            student_name_entry.focus()
            #Show toast
            fullname_message.show_toast()
            
        elif student_age_entry.get() == '':
            student_age_entry.config(bootstyle='danger')
            student_age_entry.focus()
            #Show toast
            age_message.show_toast()
        
        elif student_contact_entry.get() == '':
            student_contact_entry.config(bootstyle='danger')
            student_contact_entry.focus()
            #show Toast
            contact_message.show_toast()
            
        elif select_class_cb.get() == '':
            select_class_cb.config(bootstyle='danger')
            select_class_cb.focus()
            #Show toast
            class_message.show_toast()
            
        elif student_contact_entry.get() == '':
            student_contact_entry.config(bootstyle='danger')
            student_contact_entry.focus()
            #Show toast
            contact_message.show_toast()
            
        elif student_email_entry.get() == '':
            student_email_entry.config(bootstyle='danger')
            student_email_entry.focus()
            #Show toast
            email_message.show_toast()

        elif not check_invalid_email(email=student_email_entry.get().lower()):
            student_email_entry.config(bootstyle='danger')
            student_email_entry.focus()
            #Show toast
            valid_email_message.show_toast()
            
        elif account_password_entry.get() == '':
            account_password_entry.config(bootstyle='danger')
            account_password_entry.focus()
            
            #Show toast
            password_message.show_toast()
            
        else:
            
            pic_data = b''
            
            if pic_path.get() != '':
                resize_pic = Image.open(pic_path.get()).resize((100,100))
                resize_pic.save('temp_pic.png')
                
                read_data = open('temp_pic.png', 'rb')
                pic_data = read_data.read()
                read_data.close()
            
            else:
                read_data = open('images/add_student_img.png', 'rb')
                pic_data = read_data.read()
                read_data.close()
            
            add_data(id_number=student_id_entry.get(), password=account_password_entry.get(), name=student_name_entry.get(), age=student_age_entry.get(), 
                     gender=student_gender.get(), phone_number=student_contact_entry.get(), student_class=select_class_cb.get(), email=student_email_entry.get(), pic_data=pic_data)
            
            account_creation.show_toast()

    student_gender = tk.StringVar()
    class_list = ['Form 1', 'Form 2', 'Form 3', 'Form 4', 'Form 5', 'LowerSixth', 'UpperSixth']

    add_account_page_frame = tb.LabelFrame(root, bootstyle='primary')

    #add picture
    add_pic_section_frame = tb.LabelFrame(add_account_page_frame, bootstyle='primary')
    add_pic_section_frame.place(x=10, y=5, width=105, height=105)

    add_pic_btn = tb.Label(add_pic_section_frame, image=add_student_pic_icon)
    add_pic_btn.pack()
    # Bind the click event to the label
    add_pic_btn.bind("<Button-1>", open_pic)

    student_name_lb = tb.Label(add_account_page_frame, text="Enter Student Name", font=('Helvetica', 12))
    student_name_lb.place(x=5, y=130)
    

    student_name_entry = tb.Entry(add_account_page_frame, font=('Helvetica', 12), bootstyle= 'primary')
    student_name_entry.place(x=5, y=160, width=180)


    student_gender_lb = tb.Label(add_account_page_frame, text="Select Student Gender", font=('Helvetica', 12))
    student_gender_lb.place(x=5, y=210)

    male_gender_btn = tb.Radiobutton(add_account_page_frame, text='Male', bootstyle='primary', variable=student_gender, value='male')
    male_gender_btn.place(x=5, y=240)

    female_gender_btn = tb.Radiobutton(add_account_page_frame, text='Female', bootstyle='primary', variable=student_gender, value='female')
    female_gender_btn.place(x=85, y=240)

    student_gender.set('male')


    student_age_lb = tb.Label(add_account_page_frame, text="Enter Student Age", font=('Helvetica', 12))
    student_age_lb.place(x=5, y=270)

    student_age_entry = tb.Entry(add_account_page_frame, font=('Helvetica', 12), bootstyle= 'primary')
    student_age_entry.place(x=5, y=300, width=180)

    student_contact_lb = tb.Label(add_account_page_frame, text="Enter Phone Number", font=('Helvetica', 12))
    student_contact_lb.place(x=5, y=350)

    student_contact_entry = tb.Entry(add_account_page_frame, font=('Helvetica', 12), bootstyle= 'primary')
    student_contact_entry.place(x=5, y=380, width=180)

    student_class_lb = tb.Label(add_account_page_frame, text="Select Student Class", font=('Helvetica', 12))
    student_class_lb.place(x=5, y=435)

    select_class_cb = tb.Combobox(add_account_page_frame, bootstyle='primary', font=('Helvetica', 12), state="readonly", values=class_list)
    select_class_cb.place(x=5, y=465, width=180, height=30)

    student_id_lb = tb.Label(add_account_page_frame, text='Student ID Number:', font=('Helvetica', 12))
    student_id_lb.place(x=235, y=25)

    student_id_entry = tb.Entry(add_account_page_frame, font=('Helvetica', 14))
    student_id_entry.place(x=380, y=20, width=80, height=30)

    
    student_id_entry.config(state='readonly')
    
    generate_id_number()

    id_info_lb = tb.Label(add_account_page_frame, text="""Automatically Generated ID Number
! Remember using this ID Number
For Student to Login.""", justify=tk.LEFT, bootstyle='warning', font=('Helvetica', 8))
    id_info_lb.place(x=240, y=65)


    student_email_lb = tb.Label(add_account_page_frame, text="Enter Student Email", font=('Helvetica', 12))
    student_email_lb.place(x=240, y=130)

    student_email_entry = tb.Entry(add_account_page_frame, font=('Helvetica', 12), bootstyle= 'primary')
    student_email_entry.place(x=240, y=160, width=180)

    email_info_lb = tb.Label(add_account_page_frame, text="""Via Email Address Student
Can Recover Account
! In case Forgetting Password and also
Student will get Future Notifications.""", justify=tk.LEFT, bootstyle='warning', font=('Helvetica', 8))
    email_info_lb.place(x=240, y=200)


    account_password_lb = tb.Label(add_account_page_frame, text="Create Account Password", font=('Helvetica', 12))
    account_password_lb.place(x=240, y=270)

    account_password_entry = tb.Entry(add_account_page_frame, font=('Helvetica', 12), bootstyle= 'primary')
    account_password_entry.place(x=240, y=300, width=180)

    password_info_lb = tb.Label(add_account_page_frame, text="""Via Student Create Password
And Provided Student ID Number
Student can Login into Account.""", justify=tk.LEFT, bootstyle='warning', font=('Helvetica', 8))
    password_info_lb.place(x=240, y=345)


    home_btn = tb.Button(add_account_page_frame, text='Home', bootstyle='info', command=forward_to_welcome_page)
    home_btn.place(x=240, y=465)

    submit_btn = tb.Button(add_account_page_frame, text='Submit', bootstyle='Success', command=check_input_validation)
    submit_btn.place(x=350, y=465)


    add_account_page_frame.pack(pady=5)
    add_account_page_frame.propagate(False)
    add_account_page_frame.configure(width=480, height=580)


init_database()
welcome_page()
root.mainloop()