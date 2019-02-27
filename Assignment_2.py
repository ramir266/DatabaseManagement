import sqlite3
from FunctionsDB import FunctionDB
from sql import Connection

function = FunctionDB()
sql = Connection()

sql.dbconnection()

again = True
while again:
    print
    menu_value = function.display_menu()

    while True:
        if menu_value == 1:
            function.display_student()
            again = True
            #print("Displayed Student")
            break
        elif menu_value == 2:
            function.create_student()
            again = True
            break
        elif menu_value == 3:
            function.update_student()
            again = True
            #print("Updated Student")
            break
        elif menu_value == 4:
            function.deletestudent()
            again = True
            #print("Deleted Student")
            break
        elif menu_value == 5:
            function.search_student()
            again = True
            #print("Searched Student")
            break
        elif menu_value == 6:
            print ("Exit")
            again = False
            break

