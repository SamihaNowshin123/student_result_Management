
# Student Result Mnagement
 

The Student Result Management System is a Python-based application designed to help institutions manage student results efficiently. The system supports functionalities such as adding new results, searching for specific student records, viewing detailed reports, and role-based permissions for teachers and students. The project is built using Python's Tkinter library for the GUI and SQLite for database management. Additionally, it uses various other libraries for calculations, data manipulation, and visualization.


## Key Features

- Role-Based Access Control:

  Students can view their own results and update their information  but cannot delete records.

  Teachers can manage student records fully, including adding, updating, and deleting results.
- Student & Teacher Seperate Registration and Login
- Automatic Grade and CGPA Calculation:
   
   Based on the attendance and semester marks, the system automatically calculates the percentage, grade, and CGPA of the students.
- Search Functionality:

  Teachers can search for any student’s result by roll number.   Students can only search for their own results after logging in.




## Screenshots
![image alt](https://github.com/SamihaNowshin123/student_result_Management/blob/3b47dac611fe87ca69ac6e7da1b0bc98542f8a2e/ScreenshotFolder/Screenshot%20(270).png)
![image alt](https://github.com/SamihaNowshin123/student_result_Management/blob/de663e7fa36ae4c18d7e5097fe00435e81aae08e/ScreenshotFolder/Screenshot%20(271).png)

![image alt](https://github.com/SamihaNowshin123/student_result_Management/blob/de663e7fa36ae4c18d7e5097fe00435e81aae08e/ScreenshotFolder/Screenshot%20(273).png)

![image alt](https://github.com/SamihaNowshin123/student_result_Management/blob/297fd69a0c9031eff5f48f4ce916ce3e76ee52fc/ScreenshotFolder/Screenshot%202024-10-25%20010100.png)


## Installation

Install Python 3.12:

Ensure you have Python 3.12 installed. If not, download and install it from the official Python website.

Clone the Repository:

Clone the project repository using:

```bash
  git clone <repository-url>
```


Install the required packages using pip: 
```bash
  pip install -r requirements.txt
```

Run the Application:

Use PyCharm or another preferred IDE to open the project directory. Run the main Python file (main.py) to launch the application.

Database Setup:

Ensure that the SQLite database is correctly set up. The necessary database tables will be created upon the first run if they don't already exist. Make sure to adjust the database settings in the db.py file if necessary.


### System Requirements

| Component            | Version/Details                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **IDE**              | PyCharm 2023 or later (Recommended for better organization, linting, and debugging) |
| **Python Version**   | 3.12                                                                            |
| **Installed Packages** |                                                                               |
| `Django`             | 5.1.1                                                                           |
| `asgiref`            | 3.8.1                                                                           |
| `contourpy`          | 1.3.0                                                                           |
| `cycler`             | 0.12.1                                                                          |
| `fonttools`          | 4.54.1                                                                          |
| `image`              | 1.5.33                                                                          |
| `imagetk`            | 0.1.2                                                                           |
| `kiwisolver`         | 1.4.7                                                                           |
| `numpy`              | 2.11.1                                                                          |
| `packaging`          | 24.1                                                                            |
| `pandas`             | 2.2.2                                                                           |
| `pillow`             | 10.4.0                                                                          |
| `pip`                | 23.2.1                                                                          |
| `pyparsing`          | 3.1.4                                                                           |
| `python-dateutil`    | 2.9.0.post0                                                                     |
| `pytz`               | 2024.1                                                                          |
| `scipy`              | 1.14.1                                                                          |
| `six`                | 1.16.0                                                                          |
| `sqlparse`           | 0.5.1                                                                           |
| `tzdata`             | 2024.1                                                                          |

## Optimizations

1.Support for Multiple Courses per Student:

Currently, each student can only register for one course at a time. In future updates, we aim to allow students to enroll in multiple courses.

2.Teacher’s Dashboard for Viewing All Students in a Course:

Teachers can only view individual students' results. Future improvements will introduce a dashboard feature that allows teachers to view and manage the entire list of students enrolled in a specific course, making class management more efficient.

3.Cumulative CGPA Calculation:

The system currently calculates individual subject grades. In an upcoming version, we aim to introduce a cumulative CGPA feature. 

