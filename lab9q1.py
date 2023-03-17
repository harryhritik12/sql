import mysql.connector as sqltor

mydb = sqltor.connect(
  host="localhost",
  user="root",
  password="hritikpankaj",
  database='db'
)

mycursor = mydb.cursor()

#table=input("enter table name:")
#query="show tables"


#mycursor.execute(
 ##       '''create table student1(
	#       snum numeric(9,0) primary key,
	 #    sname varchar(30),
    #	   major varchar(25),
	 #      standing varchar(2),
	  #     age numeric(3,0)
	#);'''
    #)
#mycursor.execute('''create table Newenrolled(
#	snum numeric(9,0),
#	cname varchar(40),
#	primary key(snum,cname),
##	foreign key(cname) references class(name)
#	);'''
 # )
while(True):
    try:
        snum = input("Enter the student's roll no...:   ")
        sname=input("enter the student's name /for exit type q: ")
        major=input('enter student major: ')
        standing=input('enter student standing : ')
        age=input('enter student age : ')
        if sname == 'q':
            break
        
        mycursor.execute(
            "INSERT INTO Student1 (snum, sname, major, standing, age) VALUES (%s, %s, %s, %s, %s)",
            (snum, sname, major, standing, age)
        )
        mydb.commit()

    except sqltor.errors.DatabaseError as err:
          if err.errno == 1062:
              print("Duplicate Entry")
          elif err.errno == 1406:
              print("Maximum length exceeded. Try again.")
          elif err.errno == 1146:
              print("Table not found.")
          elif err.errno == 1054:
               print("Unidentified input parameter")
          else:
              print(err)

# close the database connection
mydb.close()


  
  

