import mysql.connector as sqltor

mydb = sqltor.connect(
  host="localhost",
  user="root",
  password="hritikpankaj",
  database='db'
)

mycursor = mydb.cursor()


try:
    while(True):

        
        snum = input("Enter student roll number: ")
        sql = "SELECT papers.paper_id,papers.pdf_content FROM papers JOIN student_research ON papers.paper_id = student_research.paper_id WHERE student_research.snum = %s"
        val = (snum,)
        mycursor.execute(sql, val)
        for i, row in enumerate(mycursor):
            pdf_content = row[0]
            pdf_content = row[1]
            fi=input("enter file name wanted to store in")
            with open(fi, "wb") as f:
                f.write(pdf_content)

        br=input("if you want to exit type q, else press any key")
        if(br=='q'):
            break


    

except sqltor.errors.DatabaseError as err:
            print("Error: ", err)
# Close the database connection
mydb.close()
