from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title label for course management
        title = Label(self.root, text="COURSE MANAGEMENT", font=("goudy old style", 20, "bold"), bg="Darkblue",
                      fg="White").place(x=10, y=15, width=1180, height=40)

        # Variables for course data
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # Widgets for data input fields (course name, duration, charges, description)
        lbl_CourseName = Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg='white').place(
            x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg='white').place(x=10,
                                                                                                                 y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg='white').place(x=10,
                                                                                                               y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg='white').place(
            x=10, y=180)

        # Entry fields for data input
        self.text_CourseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'),
                                     bg='lightyellow')
        self.text_CourseName.place(x=150, y=60, width=200)
        text_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'),
                              bg='lightyellow').place(x=150, y=100, width=200)
        text_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, 'bold'),
                             bg='lightyellow').place(x=150, y=140, width=200)
        self.text_description = Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_description.place(x=150, y=180, width=500, height=100)

        # Buttons for add, update, delete, and clear operations
        self.btn_add = Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="cornflowerblue",
                              fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="steelblue",
                                 fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="dodgerblue",
                                 fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="lightskyblue",
                                fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search Panel for searching courses by name
        self.var_Search = StringVar()
        lbl_Search_CourseName = Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'),
                                      bg='white').place(x=720, y=60)
        text_Search_CourseName = Entry(self.root, textvariable=self.var_Search, font=("goudy old style", 15, 'bold'),
                                       bg='lightyellow').place(x=850, y=60, width=180)
        btn_Search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="cornflowerblue",
                            fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

        # Frame for displaying the course table
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        # Scrollbars for the course table
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("Cid", "Name", "Duration", "Charge", "Description"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        # Setting the headings and column widths for the course table
        self.CourseTable.heading("Cid", text="CourseID")
        self.CourseTable.heading("Name", text="Name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable.heading("Charge", text="Charge")
        self.CourseTable.heading("Description", text="Description")
        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("Cid", width=100)
        self.CourseTable.column("Name", width=100)
        self.CourseTable.column("Duration", width=100)
        self.CourseTable.column("Charge", width=100)
        self.CourseTable.column("Description", width=130)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        # Display all courses initially
        self.show()

    # Function to clear all input fields and reset them to default
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_Search.set("")
        self.text_description.delete('1.0', END)
        self.text_CourseName.config(state=NORMAL)

    # Function to delete a course from the database based on the selected course name
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select course from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you Really Want to Delete?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from course where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Function to get course data from the table when a course is selected by the user
    def get_data(self, ev):
        self.text_CourseName.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.text_description.delete('1.0', END)
        self.text_description.insert(END, row[4])

    # Function to add a new course to the database
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course Name Already Present", parent=self.root)
                else:
                    cur.execute("insert into Course(name, duration, charges, description) values(?, ?, ?, ?)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.text_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Function to update the details of an existing course in the database
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Course from List", parent=self.root)
                else:
                    cur.execute("Update course set duration=?, charges=?, description=? where name=?", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.text_description.get("1.0", END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Function to search and display courses based on course name input
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course where name LIKE '%" + str(self.var_Search.get()) + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Function to display all courses in the table
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
