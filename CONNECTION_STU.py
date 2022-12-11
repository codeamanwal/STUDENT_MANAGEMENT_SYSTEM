import mysql.connector
csn=mysql.connector.connect(host="localhost",
                            user="root",
                            password="1234",
                            database="STUDENT_MANAGEMENT")
cur=csn.cursor()
cur.execute("Create table STUDENTS_DATA(Session varchar(30),SName char(30),SClass int,SSection char(20),SRollNo int,Subject1 char(40),Subject2 char(40),Subject3 char(40))")
print("Table created successfully....")
