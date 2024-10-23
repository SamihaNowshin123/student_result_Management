

from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Add Student Results", font=("goudy old style", 20, "bold"), bg="orange",
                      fg="#262626").place(x=10, y=15, width=1180, height=50)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_ctattendence = StringVar()
        self.var_semistermarks = StringVar()
        self.var_full_marks = "100"  # Auto-set Full Marks to 100

        self.roll_list = []
        self.fetch_roll()  # Call method to fetch student roll numbers

        # Widgets
        lbl_select = Label(self.root, text="Select Students", font=("goudy old style", 15, 'bold'), bg='white').place(
            x=50, y=80)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=130)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white').place(x=50,
                                                                                                             y=190)
        lbl_CT_Attendence = Label(self.root, text="CT Attendence", font=("goudy old style", 15, 'bold'),
                                  bg='white').place(x=50, y=250)
        lbl_semister = Label(self.root, text="Semester Final Marks", font=("goudy old style", 15, 'bold'),
                             bg='white').place(x=50, y=310)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list,
                                        font=("goudy old style", 15, 'bold'))
        style = ttk.Style()
        style.configure('TCombobox', background='lightyellow')
        self.txt_student.place(x=280, y=80, width=200)
        self.txt_student.set("Select")

        # Search Panel
        btn_Search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="cornflowerblue",
                            fg="white", cursor="hand2", command=self.search).place(x=500, y=80, width=120, height=28)
        text_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, 'bold'), bg='lightyellow',
                          state='readonly').place(x=280, y=130, width=340)
        text_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'),
                            bg='lightyellow', state='readonly').place(x=280, y=190, width=340)
        text_ctattendence = Entry(self.root, textvariable=self.var_ctattendence, font=("goudy old style", 15, 'bold'),
                                  bg='lightyellow').place(x=280, y=250, width=340)
        text_semistermarks = Entry(self.root, textvariable=self.var_semistermarks, font=("goudy old style", 15, 'bold'),
                                   bg='lightyellow').place(x=280, y=310, width=340)

        # Buttons
        self.btn_add = Button(self.root, text='Submit', font=("times new roman", 15, "bold"), bg="lightgreen",
                              activebackground="lightgreen", cursor="hand2", command=self.add)
        self.btn_add.place(x=300, y=420, width=120, height=35)
        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="lightgray",
                                activebackground="lightgray", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=430, y=420, width=120, height=35)

    # Fetch the list of student roll numbers from the database
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])  # Add roll numbers to the list
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Search for student details (name, course) based on roll number
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])  # Set name
                self.var_course.set(row[1])  # Set course
            else:
                messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Add new student result to the database
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # Validate if fields are filled
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please search student record", parent=self.root)
            elif self.var_ctattendence.get() == "":
                messagebox.showerror("Error", "CT Attendance Marks should be required", parent=self.root)
            elif self.var_semistermarks.get() == "":
                messagebox.showerror("Error", "Semester Marks should be required", parent=self.root)
            else:
                # Calculate percentage
                per = (int(self.var_ctattendence.get()) + int(self.var_semistermarks.get())) * 100 / int(
                    self.var_full_marks)

                # Determine CGPA and Grade based on the percentage
                if per >= 80:
                    cgpa = 4.00
                    grade = "A+"
                elif per >= 75:
                    cgpa = 3.75
                    grade = "A"
                elif per >= 70:
                    cgpa = 3.50
                    grade = "A-"
                elif per >= 65:
                    cgpa = 3.25
                    grade = "B+"
                elif per >= 60:
                    cgpa = 3.00
                    grade = "B"
                elif per >= 55:
                    cgpa = 2.75
                    grade = "B-"
                elif per >= 50:
                    cgpa = 2.50
                    grade = "C+"
                elif per >= 45:
                    cgpa = 2.25
                    grade = "C"
                elif per >= 40:
                    cgpa = 2.00
                    grade = "D"
                else:
                    cgpa = 0.00
                    grade = "F"

                # Check if the result already exists for the student and course
                cur.execute("select * from result where roll=? and course=?",
                            (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result Already Present", parent=self.root)
                else:
                    # Insert new result into the database
                    cur.execute(
                        "insert into result (Roll, Name, Course, Ctattendence, Semistermarks, Full_marks, Per, Cgpa, Grade) values (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_ctattendence.get(),
                            self.var_semistermarks.get(),
                            self.var_full_marks,  # Always 100
                            str(per),
                            str(cgpa),
                            grade
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
                    self.clear()  # Clear form after submission
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Clear the input fields
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_ctattendence.set("")
        self.var_semistermarks.set("")


if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
