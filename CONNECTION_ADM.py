import mysql.connector
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="1234",
                            database="STUDENT_MANAGEMENT")
cur=con.cursor()
cur.execute("Create table ADMISSION(AdminNo int,RollNo int,SName char(30),Address varchar(40),Phone char(20),STD int)")
print("Table created successfully....")
