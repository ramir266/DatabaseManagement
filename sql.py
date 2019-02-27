import sqlite3

class Connection:

    def dbconnection(self):
        # Connecting to a Database
        conn = sqlite3.connect('StudentDB.db')
        c = conn.cursor()
        print("Opened database successfully")

        # Creating Table
        c.execute("CREATE TABLE IF NOT EXISTS Student("
                  "StudentId INTEGER PRIMARY KEY AUTOINCREMENT,"
                  "FirstName varchar(25),"
                  "LastName varchar(25),"
                  "GPA REAL, "
                  "Major varchar(10), "
                  "FacultyAdvisor varchar(10));")
        conn.commit()