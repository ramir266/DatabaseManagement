import sqlite3
from Student import Student

student = Student()

#Connecting to a Database
conn = sqlite3.connect('StudentDB.db')
c = conn.cursor()
print("Opened database successfully")

#Creating Table
c.execute("CREATE TABLE IF NOT EXISTS Student("
          "StudentId INTEGER PRIMARY KEY AUTOINCREMENT,"
          "FirstName varchar(25),"
          "LastName varchar(25),"
          "GPA REAL, "
          "Major varchar(10), "
          "FacultyAdvisor varchar(10));")
conn.commit()

again = True
while again:
    print
    menu_value = student.display_menu()

    while True:
        if menu_value == 1:
            student.display_student()
            again = True
            #print("Displayed Student")
            break
        elif menu_value == 2:
            student.create_student()
            again = True
            break
        elif menu_value == 3:
            student.update_student()
            again = True
            #print("Updated Student")
            break
        elif menu_value == 4:
            student.deletestudent()
            again = True
            #print("Deleted Student")
            break
        elif menu_value == 5:
            student.search_student()
            again = True
            #print("Searched Student")
            break
        elif menu_value == 6:
            print ("Exit")
            again = False
            break

