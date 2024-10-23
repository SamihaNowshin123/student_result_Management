from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class StudentClass:
    def __init__(self, root, role, user_roll=None):
        self.root = root
        self.role = role
        self.user_roll = user_roll
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        self.root.grab_set()

        # Title
        title = Label(self.root, text="MANAGE STUDENT DETAIL", font=("goudy old style", 20, "bold"), bg="Darkblue", fg="White").place(x=10, y=15, width=1180, height=40)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_admission = StringVar()

        if self.role == 'Student' and self.user_roll:
            self.var_roll.set(self.user_roll)
            self.fetch_student_data(self.user_roll)

        # Widgets
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=100)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=180)
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=220)

        # Entry Fields
        self.text_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_roll.place(x=150, y=60, width=200)

        # Disable the roll number field for students
        if self.role == 'Student':
            self.text_roll.config(state='readonly')

        text_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=100, width=200)
        text_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=140, width=200)

        self.text_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), font=("goudy old style", 15, 'bold'), state='readonly', justify=CENTER)
        self.text_gender.place(x=150, y=180, width=200)
        self.text_gender.set("Select")

        self.text_address = Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_address.place(x=150, y=220, width=500, height=150)

        # Column 2
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=100)
        lbl_admission = Label(self.root, text="Admission", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=180)

        # Entry Fields for Column 2
        self.course_list = []
        self.fetch_course()
        self.text_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_dob.place(x=480, y=60, width=200)
        text_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=480, y=100, width=200)
        text_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=480, y=140, width=200)
        self.text_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, state='readonly', justify=CENTER, font=("goudy old style", 15, 'bold'))
        self.text_course.place(x=480, y=180, width=200)
        self.text_course.set("Select")

        # Buttons
        self.btn_add = Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="cornflowerblue", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="steelblue", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        # Disable delete button for students
        self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="dodgerblue", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="lightskyblue", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search Panel
        if self.role == 'Teacher':
            self.var_Search = StringVar()
            lbl_Search_roll = Label(self.root, text="Roll Number", font=("goudy old style", 15, 'bold'), bg='white').place(x=720, y=60)
            text_Search_roll = Entry(self.root, textvariable=self.var_Search, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=850, y=60, width=180)
            btn_Search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="cornflowerblue", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

            # Table Frame
            self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
            self.C_Frame.place(x=720, y=100, width=470, height=340)

            scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
            scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

            self.CourseTable = ttk.Treeview(self.C_Frame, columns=("Roll", "Name", "Email", "Gender", "DOB", "Contact", "Admission", "Course", "Address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
            scrollx.pack(side=BOTTOM, fill=X)
            scrolly.pack(side=RIGHT, fill=Y)
            scrollx.config(command=self.CourseTable.xview)
            scrolly.config(command=self.CourseTable.yview)

            self.CourseTable.heading("Roll", text="Roll No")
            self.CourseTable.heading("Name", text="Name")
            self.CourseTable.heading("Email", text="Email")
            self.CourseTable.heading("Gender", text="Gender")
            self.CourseTable.heading("DOB", text="DOB")
            self.CourseTable.heading("Contact", text="Contact")
            self.CourseTable.heading("Admission", text="Admission")
            self.CourseTable.heading("Course", text="Course")
            self.CourseTable.heading("Address", text="Address")

            self.CourseTable["show"] = 'headings'
            self.CourseTable.column("Roll", width=100)
            self.CourseTable.column("Name", width=100)
            self.CourseTable.column("Email", width=100)
            self.CourseTable.column("Gender", width=100)
            self.CourseTable.column("DOB", width=100)
            self.CourseTable.column("Contact", width=100)
            self.CourseTable.column("Admission", width=100)
            self.CourseTable.column("Course", width=100)
            self.CourseTable.column("Address", width=200)

            self.CourseTable.pack(fill=BOTH, expand=1)
            self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

            # Show the table only if the role is Teacher
            self.show()


# Fetch the list of courses from the database
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("Select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

# Add a new student to the database
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
            else:
                cur.execute("select * from student where Roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    if self.role == 'Student':
                        messagebox.showerror("Error", "You can only add your details once.", parent=self.root)
                    else:
                        messagebox.showerror("Error", "Roll Number already present", parent=self.root)
                else:
                    if self.role == 'Student' and self.var_roll.get() != self.user_roll:
                        messagebox.showerror("Error", "You cannot add another roll number.", parent=self.root)
                    else:
                        cur.execute(
                            "insert into student(Roll, Name, Email, Gender, DOB, Contact, Admission, Course, Address) "
                            "values(?,?,?,?,?,?,?,?,?)",
                            (
                                self.var_roll.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_contact.get(),
                                self.var_a_date.get(),
                                self.var_course.get(),
                                self.text_address.get('1.0', END),
                            ))
                        con.commit()
                        messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    if self.role == 'Teacher':
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

 # Update existing student information in the database
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                if self.role == 'Student' and self.var_roll.get() != self.user_roll:
                    messagebox.showerror("Error", "You cannot update another student's details", parent=self.root)
                    return

                cur.execute("select * from student where Roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select student from list", parent=self.root)
                else:
                    cur.execute(
                        "update student set Name=?, Email=?, Gender=?, DOB=?, Contact=?, Admission=?, Course=?, Address=? where Roll=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_a_date.get(),
                            self.var_course.get(),
                            self.text_address.get('1.0', END),
                            self.var_roll.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Updated Successfully", parent=self.root)
                if self.role == 'Teacher':
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

# Delete a student from the database
    def delete(self):
        # Check if the user is a student and deny deletion
        if self.role == 'Student':
            messagebox.showerror("Error", "Students are not allowed to delete records.", parent=self.root)
            return  # Exit the function early if the user is a student

        # Continue deletion process for teachers
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
            else:
                cur.execute("select * from student where Roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Roll No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op is True:
                        cur.execute("delete from student where Roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

# Clear the input fields
    def clear(self):
        # self.show()
        if self.role == 'Teacher':
            self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.text_address.delete('1.0', END)
        self.text_roll.config(state=NORMAL)



    def get_data(self, ev):
      if self.role == 'Teacher':
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

        # Check if the selected row corresponds to the logged-in student's roll number
        # if self.role == 'Student' and row[0] != self.user_roll:
        #     messagebox.showerror("Error", "You can not change information from the course Table", parent=self.root)
        #     return

        # If the user is a teacher or the logged-in student, populate the fields
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])

        self.text_address.delete("1.0", END)
        self.text_address.insert(END, row[8])

        # If the user is a student, make the roll number field readonly
        # if self.role == 'Student':
        #     self.text_roll.config(state='readonly')
        # else:
        #     self.text_roll.config(state=NORMAL)

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
# Search for a student by roll number
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from student where Roll LIKE '%{self.var_Search.get()}%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
# Fetch student data based on the provided roll number

    def fetch_student_data(self, roll_number):
        # This function will fetch and populate the student details
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT Name, Email, Contact, Address FROM student WHERE Roll=?", (roll_number,))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_email.set(row[1])
                self.var_contact.set(row[2])
                # self.text_address.delete('1.0', END)  # Clear any existing text before inserting
                # self.text_address.insert('1.0', row[3])
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching data: {str(ex)}", parent=self.root)
        finally:
            con.close()




