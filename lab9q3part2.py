import mysql.connector as sqltor

mydb = sqltor.connect(
    host="localhost",
    user="root",
    password="hritikpankaj",
    database="db"
)

# Create the papers table with a BLOB column for storing PDF files
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE papers (paper_id VARCHAR(40) PRIMARY KEY, title VARCHAR(500), pdf_content LONGBLOB)")
mycursor.execute("CREATE TABLE student_research (snum NUMERIC(9,0), paper_id VARCHAR(40), FOREIGN KEY (paper_id) REFERENCES papers(paper_id))")
try:
    while( True):
# Insert a PDF file into the papers table
        file_path=input("Enter file name: ")
        paper_id=input("Enter paper id: ")
        title=input("Enter title: ")
        if(paper_id=='q'):
            break
        
        with open(file_path, 'rb') as file:
            pdf_content = file.read()

        sql = "INSERT INTO papers (paper_id, title, pdf_content) VALUES (%s, %s, %s)"
        val = (paper_id, title, pdf_content)
        mycursor.execute(sql, val)
        mydb.commit()


        snum=input("Enter student roll...: ")
        spaper_id=input("Enter paper_id")
        if(snum=="q"):
            break
        values_to_insert = [(snum, spaper_id)]
        mycursor.executemany('INSERT INTO student_research (snum, paper_id) VALUES (%s, %s)', values_to_insert)

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
mydb.commit()

# Close the database connection
mydb.close()
