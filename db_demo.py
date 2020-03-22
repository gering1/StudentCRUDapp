import sqlite3
from Student import Student

conn = sqlite3.connect("Assignment2Student")
c = conn.cursor()

def createStudentInfo():
    complete = False
    newStudent = Student()
    while not complete:
        try:
            newStudent.sID = int(input("Enter student ID ")) #get ID
        except ValueError:
            print("Student ID must be a positive integer")
            continue

        newStudent.firstName = input("Enter first name ") #get first name
        newStudent.lastName = input("Enter last name ") #get last name
        if not newStudent.firstName.isalpha() or not newStudent.lastName.isalpha():
            print("First name and last name must contain only characters")
            continue
        try:
            newStudent.gpa = float(input("Enter GPA"))
            if newStudent.gpa<0 or newStudent.gpa>5:
                print("GPA must be between 0 and 5.0")
                continue
        except ValueError:
            print("Must be a decimal number")
            continue

        newStudent.major = input("Enter major") #get major
        if not newStudent.major.strip().isalpha():
            print("Major must only contain letters")
            continue

        newStudent.facultyAdvisor = input("Enter faculty advisor ") #get facult advisor
        if not newStudent.facultyAdvisor.isalpha():
            print("Faculty advisor must only contain letters")

        c.execute("INSERT INTO Student (StudentId,FirstName, LastName,GPA,Major,FacultyAdvisor,isDeleted)VALUES(?,?,?,?,?,?,?)",(newStudent.getStudentTuple()))
        conn.commit()
        complete = True

def updateStudentInfo():
    complete = False
    while not complete:
        choice = input("Enter 'major' to update major\nEnter 'advisor to update attribute\nEnter 'exit' to go back to menu ")
        if choice == "exit":
            complete = True
        if choice != "major" and choice != "advisor":
            print("enter major or advisor")
            continue
        updatedEntry = input("Enter updated " + choice)
        id = input("Enter ID of student you'd like to update ")
        updateTuple = (updatedEntry,id)
        if choice == "major":
            c.execute("UPDATE Student set major = ? WHERE StudentId = ?",updateTuple)
        elif choice == "advisor":
            c.execute("UPDATE Student set FacultyAdvisor = ? WHERE StudentId = ? ",updateTuple)
        conn.commit()


def deleteStudentInfo():
    id = input("Enter id of student you want to delete")
    c.execute("UPDATE Student set isDeleted = 1 WHERE StudentId = ?",(id))
    conn.commit()

def searchStudentInfo():

    complete = False
    while not complete:
        choice = input("Enter 'Major' to search by major,\nEnter 'GPA' to search by GPA,\nEnter 'Advisor' to search by "
                       "Advisor,\nEnter 'exit' to go back to menu ")
        search = input("Enter search ")
        if choice == "aMjor":
            c.execute("SELECT * FROM Student WHERE Major = ?", (search,))
            all_rows = c.fetchall()
            print(all_rows)
        elif choice == "GPA":
            c.execute("SELECT * FROM Student WHERE GPA = ?", (search,))
            all_rows = c.fetchall()
            print(all_rows)
        elif choice == "Advisor":
            c.execute("SELECT * FROM Student WHERE FacultyAdvisor = ? ", (search,))
            all_rows = c.fetchall()
            print(all_rows)
        elif choice == "exit":
            complete = True
        else:
            print("Invalid input")
            continue

exit = False
while not exit:
    choice = input("Enter '1' to display students and all their attributes\nEnter '2' to create a Student\nEnter '3' "
                   "to update Major or Advisor\nEnter '4' for student deletion\nEnter '5' to search for a "
                   "student\nEnter 'exit' to quit the application ")
    if choice == "1":
        c.execute("SELECT * FROM Student ")
        all_rows = c.fetchall()
        print(all_rows)
    elif choice == "2":
        createStudentInfo()
    elif choice == "3":
        updateStudentInfo()
    elif choice == "4":
        deleteStudentInfo()
    elif choice == "5":
        searchStudentInfo()
    elif choice == "exit":
        exit = True
