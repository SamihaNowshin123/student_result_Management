

import sqlite3
from tkinter import *
from tkinter import messagebox


class ReportClass:
    def __init__(self, root, user_role, user_roll):
        self.root = root
        self.user_role = user_role
        self.user_roll = user_roll
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="View Student Result", font=("goudy old style", 20, "bold"), bg="orange",
                      fg="#262626").place(x=10, y=15, width=1180, height=50)

        # Search
        self.var_search = StringVar()
        self.var_id = ""

        lbl_search = Label(self.root, text="Search By Roll No:", font=("goudy old style", 20, 'bold'),
                           bg='white').place(x=280, y=100)

        self.txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20),
                                bg='lightyellow')
        self.txt_search.place(x=520, y=100, width=150)
        btn_Search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="cornflowerblue",
                            fg="white", cursor="hand2", command=self.search).place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="gray", fg="white",
                           cursor="hand2", command=self.clear).place(x=800, y=100, width=100, height=35)

        # Result Labels
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                         relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                         relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                           relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                          relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_totalmarks = Label(self.root, text="Grade", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                               relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_cgpa = Label(self.root, text="CGPA", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                         relief=GROOVE).place(x=900, y=230, width=150, height=50)

        self.roll = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.grade = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.grade.place(x=750, y=280, width=150, height=50)
        self.cgpa = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.cgpa.place(x=900, y=280, width=150, height=50)

        # Button Delete
        if self.user_role == 'Teacher':
            self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="red",
                                     fg="white", cursor="hand2", command=self.delete)
            self.btn_delete.place(x=500, y=350, width=150, height=35)
        # Disable delete button for students

        # Automatically fetch student result if logged in as a student
        if self.user_role == 'Student':
            self.var_search.set(self.user_roll)  # Automatically set the student's roll number
            self.search()  # Trigger the search function to auto-fetch the result
            self.txt_search.config(state='disabled')

    # Search Function: Searches for the student result based on roll number.
    # If the user is a student, they can only search their own result.
    # It fetches the result and displays the details if found.
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            roll_no = self.var_search.get()
            if roll_no == "":
                messagebox.showerror("Error", "Roll No. Should be required", parent=self.root)
            elif self.user_role == 'Student' and roll_no != self.user_roll:
                messagebox.showerror("Error", "You can only search your own result", parent=self.root)
            else:
                cur.execute("select * from Result where Roll=?", (roll_no,))
                row = cur.fetchone()
                if row is not None:
                    self.var_id = row[0]  # Set the ID for deletion
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    marks_obtained = int(row[4]) + int(row[5])
                    self.marks.config(text=str(marks_obtained))
                    self.cgpa.config(text=row[8])
                    self.grade.config(text=row[9])
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Clear Function: Clears all the result fields and resets the form.
    # For students, it also re-enables the search input if cleared.
    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.grade.config(text="")
        self.cgpa.config(text="")
        self.var_search.set("")
        # Re-enable search if student clears the form
        if self.user_role == 'Student':
            self.txt_search.config(state='normal')

    # Delete Function: Allows the teacher to delete the result based on the searched student's roll number.
    # If a student attempts to delete, they are shown an error message.
    # The function confirms the deletion before executing it.
    def delete(self):
        if self.user_role == 'Student':
            messagebox.showerror("Error", "You are not authorized to delete results", parent=self.root)
            return

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search Student Result First", parent=self.root)
            else:
                cur.execute("select * from Result where cid=?", (self.var_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you Really Want to Delete?", parent=self.root)
                    if op:
                        cur.execute("Delete from Result where cid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Show a message for students indicating they are not allowed to delete results.
    def show_no_delete_message(self, event):
        messagebox.showinfo("Info", "As a student, you are not allowed to delete results", parent=self.root)
