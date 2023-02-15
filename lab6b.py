import mysql.connector as sqltor

mydb = sqltor.connect(
  host="localhost",
  user="root",
  password="hritikpankaj",
  database='db'
)

mycursor = mydb.cursor()

#table=input("enter table name:")
query="show tables"

try :
  print("TAbles:")
  mycursor.execute(query)
  myresult=mycursor.fetchall()
  for x in myresult:
        for y in x:
            print(">>>", end = " ")
            print(y, end=" \t ")
        print()

  table=input("table name:") 
  name =input("name ")
  #query2="select * from "+ table +" where "+ " room ="+roomno
  query2 = "SELECT room ,  meets_at FROM {} WHERE name = '{}'".format(table, name)
  mycursor.execute(query2)
  my_result=mycursor.fetchall()
  for x in my_result:
        for y in x:
            print(y, end=" \t ")
        print()

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
mydb.close()
