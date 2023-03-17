import mysql.connector as sqltor

mydb = sqltor.connect(
  host="localhost",
  user="root",
  password="hritikpankaj",
  database='db'
)

mycursor = mydb.cursor()

while True:
    snum = input("Enter the student id / for exit type q: ")
    if snum == 'q':
        break

    # Check if the student exists in Student1
    mycursor.execute("SELECT * FROM Student1 WHERE snum=%s", (snum,))
    student = mycursor.fetchone()
    if not student:
        print("Error: Student not found.")
        continue

    # Print the student's details
    print("Student details:")
    print("Roll No.: ", student[0])
    print("Name: ", student[1])
    print("Major: ", student[2])
    print("Standing: ", student[3])
    print("Age: ", student[4])
    mycursor.execute("select * from Newenrolled")
    newenrolled = mycursor.fetchone()
    print('NewENrolled')
    print("snum :",newenrolled[0])
    print("cname",newenrolled[1])
    # Check if the student has enrolled for any classes
    mycursor.execute("SELECT * FROM NewEnrolled WHERE snum=%s", (snum,))
    classes = mycursor.fetchall()
    if not classes:
        # List the available classes and ask for enrollment
        mycursor.execute("SELECT * FROM class")
        available_classes = mycursor.fetchall()
        print("The student has not enrolled for any classes.")
        print("Available classes:")
        for cls in available_classes:
            print(cls[0], "-", cls[1])
        cname = input("Enter the name of the class to enroll: ")

        try:
            mycursor.execute("INSERT INTO NewEnrolled (snum, cname) VALUES (%s, %s)", (snum, cname))
            mydb.commit()
            print("Enrollment successful.")
            mycursor.execute("select * from Newenrolled")
            newenrolled = mycursor.fetchone()

        except sqltor.errors.DatabaseError as err:
            print("Error: ", err)
    else:
        # Print the classes the student has enrolled for
        print("Enrolled classes:")
        for cls in classes:
            print(cls[1])
            
# Close the database connection
mydb.close()
