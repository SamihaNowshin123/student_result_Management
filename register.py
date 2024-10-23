# from tkinter import*
# from tkinter import ttk, messagebox
#
# from PIL import Image,ImageTk
# import sqlite3
# import os
#
# class Register:
#     def __init__(self,root):
#         self.cmb_quest = None
#         self.root=root
#         self.root.title("Registration Window")
#         self.root.geometry("1350x700+0+0")
#
#
#
#
#         #====BG Image====
#
#         self.bg=ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\blur4.jpg")
#
#         bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
#
#
# #=======LEFT IMage=======
#         self.lef = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\left4.jpg")
#
#         lef = Label(self.root, image=self.lef).place(x=50, y=100, width=560, height=500)
#
#
# #=========Register Frame========
#         frame1=Frame(self.root,bg="white")
#         frame1.place(x=610,y=100,width=700,height=500)
#
#
#         title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
#
#
# #
#         # =========Row1==============================
#         self.var_fname = StringVar()
#         self.var_lname = StringVar()
#
#         f_name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=50, y=100)
#         self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_fname)
#         self.txt_fname.place(x=50, y=130, width=250)
#
#         l_name = Label(frame1, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=370, y=100)
#         self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_lname)
#         self.txt_lname.place(x=370, y=130, width=250)
#
#         # ====Row2=================
#         self.var_contact = StringVar()
#         self.var_email = StringVar()
#
#         contact = Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=50, y=170)
#         self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_contact)
#         self.txt_contact.place(x=50, y=200, width=200)
#
#         email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=370, y=170)
#         self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_email)
#         self.txt_email.place(x=370, y=200, width=200)
#
#         # ==================Row3=================
#         self.var_nid = StringVar()
#         self.var_select_id = StringVar()  # Variable for Combobox
#
#         select_id = Label(frame1, text="Select Id", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=50, y=240)
#
#         self.cmb_id = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER,
#                                    textvariable=self.var_select_id)
#         self.cmb_id['values'] = ("Select", "Teacher", "Student")
#         self.cmb_id.place(x=50, y=270, width=250)
#         self.cmb_id.current(0)
#
#         unid = Label(frame1, text="Unic ID No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=370, y=240)
#         self.txt_nid = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_nid)
#         self.txt_nid.place(x=370, y=270, width=200)
#
#         # ============Row4======================
#         self.var_password = StringVar()
#         self.var_cpassword = StringVar()
#
#         password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
#             x=50, y=310)
#         self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_password)
#         self.txt_password.place(x=50, y=340, width=200)
#
#         cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
#                           fg="gray").place(
#             x=370, y=310)
#         self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray",
#                                    textvariable=self.var_cpassword)
#         self.txt_cpassword.place(x=370, y=340, width=200)
#
#         #==============Terms-------------
#         self.var_chk=IntVar()
#         chk=Checkbutton(frame1,text="I agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
#         self.btn_Register= Button(frame1, text='Register', font=("goudy old style", 15, "bold"), bg="green",
#                               fg="white", cursor="hand2",command=self.register_data)
#         self.btn_Register.place(x=50, y=420, width=180, height=40)
#         self.btn_login = Button(frame1, text='Sign In', font=("goudy old style", 15, "bold"), bg="Dark Green",
#                                    fg="white", cursor="hand2",command=self.login_window)
#         self.btn_login.place(x=350, y=420, width=180, height=40)
#
#
#
#     def login_window(self):
#         self.root.destroy()
#         os.system("python login.py")
#     def clear(self):
#         self.txt_fname.delete(0,END)
#         self.txt_lname.delete(0, END)
#         self.txt_contact.delete(0, END)
#         self.txt_email.delete(0, END)
#
#         self.txt_password.delete(0, END)
#         self.txt_cpassword.delete(0, END)
#         self.txt_nid.delete(0,END)
#         # self.cmb_quest.current(0)
#         self.cmb_id.current(0)
#
#
#     def register_data(self):
#         if self.var_fname.get() == "" or self.txt_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" \
#                 or self.cmb_id.get() == "Select" or self.txt_nid.get() == "" or self.var_password.get() == "" or self.var_cpassword.get() == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#
#         elif self.var_password.get() != self.var_cpassword.get():
#             messagebox.showerror("Error", "Password and Confirm Password must match", parent=self.root)
#             # Check if the terms and conditions checkbox is checked
#         elif self.var_chk.get() != 1:
#             messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
#
#
#         else:
#              try:
#                  con = sqlite3.connect(database="rms.db")
#                  cur = con.cursor()
#                  cur.execute("select * from employee where email=?", (self.txt_email.get(),))
#                  row = cur.fetchone()
#                  print(row)
#                  if row != None:
#                      messagebox.showerror("Error", "User Already Exist,PLaese try with another email", parent=self.root)
#                  else:
#                      cur.execute(
#                          "insert into employee(f_name,l_name,contact,email,id,nid,password) values(?,?,?,?,?,?,?)",
#                          (
#                              self.txt_fname.get(),
#                              self.txt_lname.get(),
#                              self.txt_contact.get(),
#                              self.txt_email.get(),
#                              self.cmb_id.get(),
#                              self.txt_nid.get(),
#                              self.txt_password.get()
#                          ))
#                      con.commit()
#                      con.close()
#                      messagebox.showinfo("Success", "Registered Successsfully", parent=self.root)
#                      self.clear()
#                      self.login_window()
#              except Exception as ex:
#                  messagebox.showerror("Error", f"Error due to {str(ex)}")
#
#
# root=Tk()
# obj=Register(root)
# root.mainloop()



from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class Register:
    def __init__(self, root):
        self.cmb_quest = None
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")

        # ====BG Image====
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\blur4.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # =======LEFT Image=======
        self.lef = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\left4.jpg")
        lef = Label(self.root, image=self.lef).place(x=50, y=100, width=560, height=500)

        # =========Register Frame========
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=610, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # =========Row 1: Name and Address==========
        self.var_fname = StringVar()
        self.var_lname = StringVar()

        f_name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_fname)
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_lname)
        self.txt_lname.place(x=370, y=130, width=250)

        # =========Row 2: Contact and Email==========
        self.var_contact = StringVar()
        self.var_email = StringVar()

        contact = Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_contact)
        self.txt_contact.place(x=50, y=200, width=200)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_email)
        self.txt_email.place(x=370, y=200, width=200)

        # =========Row 3: Select Role and Unique ID==========
        self.var_nid = StringVar()
        self.var_select_id = StringVar()  # Variable for Combobox

        select_id = Label(frame1, text="Select Id", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_id = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER, textvariable=self.var_select_id)
        self.cmb_id['values'] = ("Select", "Teacher", "Student")
        self.cmb_id.place(x=50, y=270, width=250)
        self.cmb_id.current(0)

        unid = Label(frame1, text="Unique ID No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_nid = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_nid)
        self.txt_nid.place(x=370, y=270, width=200)

        # =========Row 4: Password and Confirm Password==========
        self.var_password = StringVar()
        self.var_cpassword = StringVar()

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_password)
        self.txt_password.place(x=50, y=340, width=200)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_cpassword)
        self.txt_cpassword.place(x=370, y=340, width=200)

        # ============Terms and Conditions Checkbox==========
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I agree to the Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=50, y=380)

        # ============Register and Sign In Buttons==========
        self.btn_Register = Button(frame1, text='Register', font=("goudy old style", 15, "bold"), bg="green", fg="white", cursor="hand2", command=self.register_data)
        self.btn_Register.place(x=50, y=420, width=180, height=40)
        self.btn_login = Button(frame1, text='Sign In', font=("goudy old style", 15, "bold"), bg="Dark Green", fg="white", cursor="hand2", command=self.login_window)
        self.btn_login.place(x=350, y=420, width=180, height=40)

    # Function to open the login window
    def login_window(self):
        """Destroy the current window and open the login window."""
        self.root.destroy()
        os.system("python login.py")

    # Function to clear all the input fields
    def clear(self):
        """Clear all the input fields on the registration form."""
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.txt_nid.delete(0, END)
        self.cmb_id.current(0)

    # Function to handle registration
    def register_data(self):
        """Register the user by validating input data and inserting it into the database."""
        if self.var_fname.get() == "" or self.txt_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.cmb_id.get() == "Select" or self.txt_nid.get() == "" or self.var_password.get() == "" or self.var_cpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password must match", parent=self.root)

        elif self.var_chk.get() != 1:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)

        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Already Exists, Please try with another email", parent=self.root)
                else:
                    cur.execute(
                        "insert into employee(f_name, l_name, contact, email, id, nid, password) values(?,?,?,?,?,?,?)",
                        (
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_contact.get(),
                            self.txt_email.get(),
                            self.cmb_id.get(),
                            self.txt_nid.get(),
                            self.txt_password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")


root = Tk()
obj = Register(root)
root.mainloop()


