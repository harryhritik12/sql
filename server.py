import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "hritikpankaj",
    database ="db"
)

cursorOBJ = mydb.cursor()

query = "select * from student"
    
cursorOBJ.execute(query)

res = cursorOBJ.fetchall()

for x in res:
    for y in x:
        print(y, end = "\t")
    print()

mydb.close()