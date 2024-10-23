from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

from Course import CourseClass
from Student import StudentClass
from Result import ResultClass
from Report import ReportClass
import os
import sys

class RMS:
    def __init__(self, root):
        # Initializes the main window for the Student Result Management System.
        # Sets up role handling for Teacher or Student and creates the user interface with buttons
        # and background images.
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="White")

        # Role handling: Student or Teacher
        self.role = sys.argv[1] if len(sys.argv) > 1 else 'Student'
        self.student_roll = sys.argv[2] if len(sys.argv) > 2 else None  # Only passed if student

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Asus\PycharmProjects\RMSproject\blur1.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Icons for title bar
        self.photo = PhotoImage(file='logo.png')
        self.photo = self.photo.subsample(5)  # Resize the logo icon

        # Title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.photo,
                      font=("goudy old style", 20, "bold"), bg="Darkblue", fg="White").place(x=0, y=0, relwidth=1, height=50)

        # Menu Frame for buttons
        Mframe = LabelFrame(self.root, text="Menu", font=("times new roman", 15), bg="white")
        Mframe.place(x=70, y=70, width=1349, height=80)

        # Buttons for navigation based on the role (Teacher or Student)
        if self.role != 'Student':  # Only show these buttons if the user is a Teacher
            btn_course = Button(Mframe, text="Course", font=("goudy old style", 15, "bold"), bg="#1A237E", fg="White",
                                cursor="hand2", command=self.add_course)
            btn_course.place(x=20, y=5, width=200, height=40)

            btn_result = Button(Mframe, text="Entry Result", font=("goudy old style", 15, "bold"), bg="#1A237E", fg="White",
                                cursor="hand2", command=self.add_result)
            btn_result.place(x=240, y=5, width=200, height=40)

        # Common buttons for both Students and Teachers
        btn_student = Button(Mframe, text="Student", font=("goudy old style", 15, "bold"), bg="#1A237E", fg="White",
                             cursor="hand2", command=self.add_Student)
        btn_student.place(x=460 if self.role != 'Student' else 20, y=5, width=200, height=40)  # Adjust placement for Student role

        btn_view = Button(Mframe, text="View Result", font=("goudy old style", 15, "bold"), bg="#1A237E", fg="White",
                          cursor="hand2", command=self.add_report)
        btn_view.place(x=680 if self.role != 'Student' else 240, y=5, width=200, height=40)

        btn_logout = Button(Mframe, text="Logout", font=("goudy old style", 15, "bold"), bg="#1A237E", fg="White",
                            cursor="hand2", command=self.logout)
        btn_logout.place(x=900 if self.role != 'Student' else 460, y=5, width=200, height=40)

        btn_exit = Button(Mframe, text="Exit", font=("goudy old style", 15, "bold"), bg="#1A237E", fg="White",
                          cursor="hand2", command=self.exit_)
        btn_exit.place(x=1120 if self.role != 'Student' else 680, y=5, width=200, height=40)

        # Content Window
        self.image = PhotoImage(file='RMSPic.png')
        self.image = self.image.subsample(2)  # Resize image to fit the content window
        image_label = Label(self.root, image=self.image)
        image_label.place(x=250, y=230, width=1100, height=450)

        # Footer section with contact information
        footer = Label(self.root, text="For any Query Contact us 019******5",
                       font=("goudy old style", 12), bg="#1A237E", fg="White")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        # Opens the course management window. This function is only accessible by Teachers.

        if self.role == "Student":
            messagebox.showerror("Access Denied", "Students cannot access Course Management.", parent=self.root)
        else:
            self.new_win = Toplevel(self.root)  # Open a new window for course management
            self.new_obj = CourseClass(self.new_win)

    def add_Student(self):
        # Opens the student management window.
        # Both Teachers and Students can access this feature, but the functionality will vary.
        # The role and student roll are passed to manage the appropriate access level.
        self.new_win = Toplevel(self.root)  # Open a new window for student management
        self.new_obj = StudentClass(self.new_win, self.role, self.student_roll)

    def add_result(self):
        # Opens the result entry window. This function is only accessible by Teachers.

        if self.role == "Student":
            messagebox.showerror("Access Denied", "Students cannot enter results.", parent=self.root)
        else:
            self.new_win = Toplevel(self.root)  # Open a new window for result entry
            self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        # Opens the result viewing window.
        # Both Teachers and Students can access this feature, but the results shown will vary.
        # Students will only see their own results, while Teachers can view all results.
        self.new_win = Toplevel(self.root)  # Open a new window for result viewing
        self.new_obj = ReportClass(self.new_win, self.role, self.student_roll)

    def logout(self):
        # Handles the logout process. The user is prompted for confirmation before logging out.
        # If confirmed, the login window is opened, and the current session is closed.
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()  # Close the current window
            os.system("python login.py")  # Reopen the login window

    def exit_(self):
        # Handles the exit process. The user is prompted for confirmation before exiting.
        # If confirmed, the program closes.
        op = messagebox.askyesno("Confirm", "Do you really want to exit?", parent=self.root)
        if op:
            self.root.destroy()  # Close the program


if __name__ == "__main__":
    # Initializes the Tkinter window and runs the application.
    root = Tk()
    obj = RMS(root)
    root.mainloop()
