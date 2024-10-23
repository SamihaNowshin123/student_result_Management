# from tkinter import *
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
# import sqlite3
# import os
# from Student import StudentClass
#
#
# class Login:
#     def __init__(self, root):
#         self.cmb_quest = None
#         self.root = root
#         self.root.title("Login Window")
#         self.root.geometry("1350x700+0+0")
#
#         # ====BG Image====
#         self.bg = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\log5.jpg")
#         bg = Label(self.root, image=self.bg).place(x=200, y=0, relwidth=1, relheight=1)
#
#         # =======LEFT Image=======
#         self.lef = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\Logleft3.jpg")
#         lef = Label(self.root, image=self.lef).place(x=50, y=100, width=560, height=500)
#
#         # =========Register Frame========
#         login_frame = Frame(self.root, bg="white")
#         login_frame.place(x=610, y=100, width=700, height=500)
#
#         title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="steelblue").place(x=250, y=50)
#
#         email = Label(login_frame, text="Email Address", font=("times new roman", 18, "bold"), bg="white",
#                       fg="steelblue").place(x=100, y=150)
#         self.txt_email = Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgray")
#         self.txt_email.place(x=100, y=180, width=350, height=35)
#
#         pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white",
#                       fg="steelblue").place(x=100, y=250)
#         self.txt_pass = Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgray", show="*")
#         self.txt_pass.place(x=100, y=280, width=350, height=35)
#
#         btn_reg = Button(login_frame, text="Register new Account?", font=("times new roman", 16), bg="white", bd=0,
#                          fg="Pale Violet Red", cursor="hand2", command=self.register_window).place(x=100, y=320)
#         btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 16), bg="white", bd=0,
#                             fg="Red", cursor="hand2", command=self.forget_password_window).place(x=350, y=320)
#
#         btn_login = Button(login_frame, text="Login", font=("times new roman", 14), fg="white",
#                            bg="Maroon", cursor="hand2", command=self.login).place(x=100, y=360, width=180, height=40)
#
#     def register_window(self):
#         self.root.destroy()
#         import register
#
#     def reset(self):
#         self.txt_new_password.delete(0, END)
#         self.txt_c_newpassword.delete(0, END)
#         self.txt_pass.delete(0, END)
#         self.txt_email.delete(0, END)
#
#     def forget_password(self):
#         if self.txt_new_password == "":
#             messagebox.showerror("Error", "All Fields are Required", parent=self.root2)
#         elif self.txt_new_password.get() != self.txt_c_newpassword.get():
#             messagebox.showerror("Error", "Two Passwords must match", parent=self.root2)
#         else:
#             try:
#                 con = sqlite3.connect(database="rms.db")
#                 cur = con.cursor()
#                 cur.execute("select * from employee where email=?", (self.txt_email.get(),))
#                 row = cur.fetchone()
#
#                 cur.execute("update employee set password=? where email=?", (self.txt_new_password.get(), self.txt_email.get(),))
#                 con.commit()
#                 con.close()
#                 messagebox.showinfo("Success", "Your password has been reset, please log in with the new password", parent=self.root2)
#
#                 self.reset()
#                 self.root2.destroy()
#
#             except Exception as es:
#                 messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
#
#     def forget_password_window(self):
#         if self.txt_email.get() == "":
#             messagebox.showerror("Error", "Please enter an email address to reset your password", parent=self.root)
#         else:
#             try:
#                 con = sqlite3.connect(database="rms.db")
#                 cur = con.cursor()
#                 cur.execute("select * from employee where email=?", (self.txt_email.get(),))
#                 row = cur.fetchone()
#                 if row is None:
#                     messagebox.showerror("Error", "Please enter a valid email address to reset your password", parent=self.root)
#                 else:
#                     con.close()
#                     self.root2 = Toplevel()
#                     self.root2.title("Forget Password")
#                     self.root2.geometry("350x450+530+150")
#                     self.root2.config(bg="white")
#                     self.root2.focus_force()
#                     self.root2.grab_set()
#
#                     t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
#
#                     npassword = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
#                     self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
#                     self.txt_new_password.place(x=50, y=130, width=250)
#
#                     cpassword = Label(self.root2, text="Retype New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
#                     self.txt_c_newpassword = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
#                     self.txt_c_newpassword.place(x=50, y=210, width=250)
#
#                     btn_change_password = Button(self.root2, text="Reset Password", bg="green", fg="white",
#                                                  font=("Times new roman", 15, "bold"), command=self.forget_password).place(x=90, y=340)
#
#             except Exception as es:
#                 messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
#
#     def login(self):
#         if self.txt_email.get() == "" or self.txt_pass.get() == "":
#             messagebox.showerror("Error", "All Fields are required", parent=self.root)
#         else:
#             try:
#                 con = sqlite3.connect(database="rms.db")
#                 cur = con.cursor()
#                 cur.execute("select * from employee where email=? and password=?", (self.txt_email.get(), self.txt_pass.get(),))
#                 row = cur.fetchone()
#
#                 if row is None:
#                     messagebox.showerror("Error", "INVALID USERNAME & PASSWORD", parent=self.root)
#                 else:
#                     role = row[5]  # Assuming the role is stored in the 5th column
#                     student_roll = row[6]
#                     messagebox.showinfo("Success", f"Welcome, {role}", parent=self.root)
#
#                     # Pass the role and student roll number to the dashboard function
#                     self.open_dashboard(role, student_roll)
#
#             except Exception as es:
#                 messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
#
#     def open_dashboard(self, role, student_roll=None):
#         try:
#             if role == "Student":
#                 os.system(f"python dashboard.py {role} {student_roll}")
#             else:
#                 os.system(f"python dashboard.py {role}")
#
#             # Only destroy the root window after the dashboard is opened successfully
#             self.root.destroy()
#
#         except Exception as es:
#             messagebox.showerror("Error", f"Error while opening dashboard: {str(es)}", parent=self.root)
#
#
# # Initialize the Tkinter root
# root = Tk()
# obj = Login(root)
# root.mainloop()



from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os
from Student import StudentClass


class Login:
    def __init__(self, root):
        self.cmb_quest = None
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")

        # ====BG Image====
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\log5.jpg")
        bg = Label(self.root, image=self.bg).place(x=200, y=0, relwidth=1, relheight=1)

        # =======LEFT Image=======
        self.lef = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\Logleft3.jpg")
        lef = Label(self.root, image=self.lef).place(x=50, y=100, width=560, height=500)

        # =========Login Frame (main UI for login)========
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=610, y=100, width=700, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="steelblue").place(x=250, y=50)

        # =====Email Input Label and Entry======
        email = Label(login_frame, text="Email Address", font=("times new roman", 18, "bold"), bg="white", fg="steelblue").place(x=100, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_email.place(x=100, y=180, width=350, height=35)

        # =====Password Input Label and Entry======
        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="steelblue").place(x=100, y=250)
        self.txt_pass = Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgray", show="*")
        self.txt_pass.place(x=100, y=280, width=350, height=35)

        # =====Buttons for Register and Forget Password=====
        btn_reg = Button(login_frame, text="Register new Account?", font=("times new roman", 16), bg="white", bd=0, fg="Pale Violet Red", cursor="hand2", command=self.register_window).place(x=100, y=320)
        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 16), bg="white", bd=0, fg="Red", cursor="hand2", command=self.forget_password_window).place(x=350, y=320)

        # =====Login Button=====
        btn_login = Button(login_frame, text="Login", font=("times new roman", 14), fg="white", bg="Maroon", cursor="hand2", command=self.login).place(x=100, y=360, width=180, height=40)

    # =====Function to open the registration window=====
    def register_window(self):
        self.root.destroy()
        import register  # Import the registration module

    # =====Function to reset password fields and input fields after reset=====
    def reset(self):
        self.txt_new_password.delete(0, END)
        self.txt_c_newpassword.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_email.delete(0, END)

    # =====Function to handle the actual password reset=====
    def forget_password(self):
        if self.txt_new_password == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root2)
        elif self.txt_new_password.get() != self.txt_c_newpassword.get():
            messagebox.showerror("Error", "Two Passwords must match", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()

                # Update the password in the database
                cur.execute("update employee set password=? where email=?", (self.txt_new_password.get(), self.txt_email.get(),))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Your password has been reset, please log in with the new password", parent=self.root2)

                # Reset the fields and close the password reset window
                self.reset()
                self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    # =====Function to open the forget password window=====
    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter an email address to reset your password", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter a valid email address to reset your password", parent=self.root)
                else:
                    con.close()

                    # Open a new window for resetting the password
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x450+530+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

                    # New Password Input
                    npassword = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
                    self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_password.place(x=50, y=130, width=250)

                    # Confirm New Password Input
                    cpassword = Label(self.root2, text="Retype New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
                    self.txt_c_newpassword = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_c_newpassword.place(x=50, y=210, width=250)

                    # Button to trigger password reset
                    btn_change_password = Button(self.root2, text="Reset Password", bg="green", fg="white", font=("Times new roman", 15, "bold"), command=self.forget_password).place(x=90, y=340)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    # =====Login function that checks credentials and opens the dashboard based on role=====
    def login(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?", (self.txt_email.get(), self.txt_pass.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "INVALID USERNAME & PASSWORD", parent=self.root)
                else:
                    role = row[5]  # Assuming the role is stored in the 5th column
                    student_roll = row[6]  # Assuming student roll is stored in the 6th column
                    messagebox.showinfo("Success", f"Welcome, {role}", parent=self.root)

                    # Pass the role and student roll number to the dashboard function
                    self.open_dashboard(role, student_roll)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    # =====Open the dashboard window based on the user's role (Teacher or Student)=====
    def open_dashboard(self, role, student_roll=None):
        try:
            if role == "Student":
                os.system(f"python dashboard.py {role} {student_roll}")  # Open dashboard for student
            else:
                os.system(f"python dashboard.py {role}")  # Open dashboard for teacher

            # Destroy the login window after the dashboard opens
            self.root.destroy()

        except Exception as es:
            messagebox.showerror("Error", f"Error while opening dashboard: {str(es)}", parent=self.root)


# Initialize the Tkinter root
root = Tk()
obj = Login(root)
root.mainloop()

