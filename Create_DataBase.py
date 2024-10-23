
# import sqlite3
#
#
#
# import os
#
# def Create_DataBase():
#     con = sqlite3.connect(database="rms.db")
#     cur = con.cursor()
#
#     # Create Course table
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS Course (
#             cid INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             duration TEXT,
#             charges TEXT,
#             description TEXT
#         )""")
#     con.commit()
#
#     # Drop old student table if it exists and recreate it with correct schema
#     cur.execute("DROP TABLE IF EXISTS Student")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS Student (
#         Roll INTEGER PRIMARY KEY AUTOINCREMENT,
#         Name TEXT,
#         Email TEXT,
#         Gender TEXT,
#         DOB TEXT,
#         Contact TEXT,
#         Admission TEXT,
#         Course TEXT,
#         Address TEXT
#     )""")
#     con.commit()
#
#     # Drop and recreate Result table
#     cur.execute("DROP TABLE IF EXISTS Result")
#
#     # Remove commented-out code causing the issue
#     # Create Employee table for registration data
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS employee (
#             eid INTEGER PRIMARY KEY AUTOINCREMENT,
#             f_name TEXT,
#             l_name TEXT,
#             contact TEXT,
#             email TEXT,
#             id TEXT,
#             nid TEXT,
#             password TEXT
#         )
#     """)
#     con.commit()
#
#     # Confirm tables exist
#     cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     tables = cur.fetchall()
#     print("Tables in database:", tables)
#
#     # Create Result table
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS Result (
#             cid INTEGER PRIMARY KEY AUTOINCREMENT,
#             Roll TEXT,
#             Name TEXT,
#             Course TEXT,
#             Ctattendence TEXT,
#             Semistermarks TEXT,
#             Full_marks TEXT,
#             Per TEXT,
#             Cgpa TEXT,
#             Grade TEXT
#         )
#     """)
#     con.commit()
#
#     # Check if the employee table exists
#     cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee';")
#     table_exists = cur.fetchone()
#     if not table_exists:
#         print("The employee table does not exist.")
#     else:
#         print("The employee table exists.")
#
#     con.close()
#
#     # Print the database path to confirm file location
#     print(f"Database path: {os.path.abspath('rms.db')}")
#
# Create_DataBase()
#
import sqlite3
import os

# Function to create the necessary tables for the student result management system
def Create_DataBase():
    # Establish connection to SQLite database, or create it if it doesn't exist
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()

    # Create Course table if it doesn't exist
    # This table stores course details like course name, duration, charges, and description
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT,
            charges TEXT,
            description TEXT
        )""")
    con.commit()

    # Drop the old Student table if it exists and recreate it with the correct schema
    # This table stores student details like Roll No, Name, Email, Gender, DOB, Contact, Admission date, Course, and Address
    cur.execute("DROP TABLE IF EXISTS Student")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        Roll INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Email TEXT,
        Gender TEXT,
        DOB TEXT,
        Contact TEXT,
        Admission TEXT,
        Course TEXT,
        Address TEXT
    )""")
    con.commit()

    # Drop and recreate the Result table
    # This table stores student result information, including roll number, name, course, attendance, semester marks, full marks, percentage, CGPA, and grade
    cur.execute("DROP TABLE IF EXISTS Result")

    # Create Employee table if it doesn't exist
    # This table stores employee information for registration, including first name, last name, contact, email, role (Teacher/Student), national ID, and password
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name TEXT,
            l_name TEXT,
            contact TEXT,
            email TEXT,
            id TEXT,
            nid TEXT,
            password TEXT
        )
    """)
    con.commit()

    # Confirm tables exist in the database by fetching their names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("Tables in database:", tables)

    # Create Result table again after removing the old one
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Result (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            Roll TEXT,
            Name TEXT,
            Course TEXT,
            Ctattendence TEXT,
            Semistermarks TEXT,
            Full_marks TEXT,
            Per TEXT,
            Cgpa TEXT,
            Grade TEXT
        )
    """)
    con.commit()

    # Check if the employee table exists and confirm its creation
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee';")
    table_exists = cur.fetchone()
    if not table_exists:
        print("The employee table does not exist.")
    else:
        print("The employee table exists.")

    # Close the database connection
    con.close()

    # Print the database file path to confirm the location of the database
    print(f"Database path: {os.path.abspath('rms.db')}")

# Call the function to create the database and tables
Create_DataBase()
