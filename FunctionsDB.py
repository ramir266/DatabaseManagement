import sqlite3
from Student import Student
student = Student()

class FunctionDB:
    def display_student(self):
        conn = sqlite3.connect('StudentDB.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Student")
        result = c.fetchall()
        for x in result:
            print(x)
        return

    def display_menu(self):
        print("1) Display all Students\n"
              "2) Create Student \n"
              "3) Update Student \n"
              "4) Delete Student \n"
              "5) Search Student \n"
              "6) Exit Student \n")
        while True:
            try:
                option = int(input("What would you like to do? (1-6): "))
                if option > 6 or option < 1:
                    raise Exception()
                break
            except Exception:
                print("Invalid Input!")
        return option

    def valid_student(self, id):
        conn = sqlite3.connect('StudentDB.db')
        c = conn.cursor()
        c.execute("SELECT StudentID from Student WHERE StudentId = " + str(id))
        student = c.fetchall()
        if student == []:
            print ("Student not in database")
            return False
        else:
            return True

    def deletestudent(self):
        conn = sqlite3.connect('StudentDB.db')
        c = conn.cursor()
        tryinput = True
        while (tryinput):
            newGPA = raw_input("Enter Student Id you want to delete: ")
            try:
                idnumber = float(newGPA)
                if not self.valid_student(idnumber):
                    print("Student ID not in Database.")
                else:
                    tryinput = False
            except ValueError:
                print("Enter a valid GPA")

        c.execute("DELETE FROM Student WHERE StudentId = {};".format(idnumber))
        conn.commit()

    def create_student(self):
        conn = sqlite3.connect('StudentDB.db')
        print("Enter student's first name: ")
        firstname = raw_input();
        print("Enter student's last name: ")
        lastname = raw_input()
        print("Enter GPA")
        gpa = raw_input()
        print("Enter student's major: ")
        major = raw_input()
        print("Enter student's faculty advisor: ")
        facultyadvisor = raw_input()

        if (firstname.isdigit() or lastname.isdigit() or major.isdigit() or facultyadvisor.isdigit()):
            print("Invalid Input. Please no digits in Name, Major, or Faculty name.")
        else:
            # student = Student(firstname, lastname, gpa, major, facultyadvisor)
            c = conn.cursor()
            c.execute("INSERT INTO Student(FirstName, LastName, GPA, Major, FacultyAdvisor)"
                      "VALUES (?,?,?,?,?)", (firstname, lastname, gpa, major, facultyadvisor))
            conn.commit()

    def update_student(self):
        conn = sqlite3.connect('StudentDB.db')
        c = conn.cursor()
        print ("Enter Student ID you would like to update: ")
        id = int(input())
        if not self.valid_student(id):
            print("Update Failed")
        else:
            # print("Let's do it.")
            while True:
                # print("What would you like to update? (Major/Advisor)")
                answer = raw_input("What would you like to update? (Major/Advisor): ")
                if answer.upper() == "MAJOR":
                    # print("this is updating major.")
                    change = raw_input("Change current Major into what?: ")
                    c.execute("UPDATE Student SET Major = ?  WHERE StudentId = ?", (change, id))
                    conn.commit()
                    print("Major updated successfully!")
                    break;
                elif answer.upper() == "ADVISOR":
                    change = raw_input("Change current Advisor with who?: ")
                    c.execute("UPDATE Student SET FacultyAdvisor = ?  WHERE StudentId = ?", (change, id))
                    conn.commit()
                    print("Faculty Advisor updated sucessfully!")
                    break;
                else:
                    print("Bad Input. Please select either Major or Advisor")

    def search_student(self):
        conn = sqlite3.connect('StudentDB.db')
        c = conn.cursor()

        while True:
            print("Search for GPA, Major, Faculty: ")
            input = raw_input()
            if input.upper() == "GPA":
                print("What GPA would you like to search?: ")
                number = raw_input()
                c.execute("SELECT * FROM Student WHERE GPA = ?",(number,))
                result = c.fetchall()
                for x in result:
                    print(x)
                break
            elif input.upper() == "MAJOR":
                print("What Major would you like to find?: ")
                majorinput = raw_input()
                c.execute("SELECT * FROM Student WHERE Major = ?", (majorinput,))
                result = c.fetchall()
                for x in result:
                    print(x)
                break
            elif input.upper() == "FACULTY":
                print("What faculty would you like to find?: ")
                facultyinput = raw_input()
                c.execute("SELECT * FROM Student WHERE FacultyAdvisor = ?", (facultyinput,))
                result = c.fetchall()
                for x in result:
                    print(x)
                break
            else:
                print("Bad Input. Please type either GPA, Major, or Faculty")