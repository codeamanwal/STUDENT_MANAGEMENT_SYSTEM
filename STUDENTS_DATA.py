# SOURCE CODE FOR STUDENT_DATA MENU.
import MAIN_MENU
import STUDENTS_DATA
import mysql.connector
def STU_MENU():
    while True:
        #student_data.clrScreen ()
        print("\t\t.................................................................................................")
        print("\t\t*******WELCOME TO STUDENT MANAGEMENT SYSTEM*********")
        print("\t\t.................................................................................................")
        print("\n\t\t*****STUDENTS DATA MENU******")
        print("1. Add Student Records")
        print("2. Show Student Details")
        print("3. Search Student Record")
        print("4. Delete Student Record")
        print("5. Edit Student Record")
        print("6. Exit")
        print("\t\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        choice=int(input("Enter your choice 1-6:"))
        if choice==1:
            STUDENTS_DATA.Add_Records()
        elif choice==2:
            STUDENTS_DATA.Show_Stu_Details()
        elif choice==3:
            STUDENTS_DATA.Search_Stu_Details()
        elif choice==4:
            STUDENTS_DATA.Delete_Stu_Details()
        elif choice==5:
            STUDENTS_DATA.Edit_Stu_Details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice try again....")
            conti="Press any key to return to Main Menu"
def Add_Records():
    while True:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="1234",
                                    database="STUDENT_MANAGEMENT")
        cursor=con.cursor()
        session=input("Enter Academic Session (eg,2019-20):")
        stname=input("Enter Student Name:")
        stclass=int(input("Enter Class:"))
        stsec=input("Enter Section:")
        stroll=int(input("Enter RollNo.:"))
        sub1=input("Enter Subject1:")
        sub2=input("Enter Subject2:")
        sub3=input("Enter Subject3:")
        query="insert into STUDENTS_DATA values('{}','{}',{},'{}',{},'{}','{}','{}')".format(session,stname,stclass,stsec,stroll,sub1,sub2,sub3)
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        print("CONGRATS!...Record has been successfully saved in student table...")
        print("THANK YOU!...")
        ch=input("Do you want to enter more records?(y/n)")
        if ch=="n":
           break
def Show_Stu_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    cursor.execute("select * from STUDENTS_DATA")
    data=cursor.fetchall()
    for row in data:
        print(row)
def Search_Stu_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter STUDENT'S NAME:")
    st="select * from STUDENTS_DATA where SName='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print("YOUR DESIRED DATA IS....")
    print(data)
    print("THANK YOU!...")
def Delete_Stu_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter STUDENT'S NAME.:")
    st="delete from STUDENTS_DATA where SName='%s'"%(ac)
    cursor.execute(st)
    con.commit()
    print("Data deleted successfully")
    print("THANK YOU!...")
def Edit_Stu_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    print("1: EDIT SESSION")
    print("2: EDIT NAME")
    print("3: EDIT CLASS")
    print("4: EDIT SECTION")
    print("5: EDIT ROLL N0.")
    print("6: EDIT SUBJECT 1")
    print("7: EDIT SUBJECT 2")
    print("8: EDIT SUBJECT 3")
    print("9: RETURN")
    print("\t\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    choice=int(input("PLEASE Enter Your Choice:"))
    if choice==1:
        STUDENTS_DATA.edit_session()
    elif choice==2:
        STUDENTS_DATA.edit_name()
    elif choice==3:
        STUDENTS_DATA.edit_class()
    elif choice==4:
        STUDENTS_DATA.edit_section()
    elif choice==5:
        STUDENTS_DATA.edit_rollno()
    elif choice==6:
        STUDENTS_DATA.edit_sub1()
    elif choice==7:
        STUDENTS_DATA.edit_sub2()
    elif choice==8:
        STUDENTS_DATA.edit_sub3()
    elif choice==9:
        return
    else:
        print("Error:   Invalid choice try again.......")
        conti="press any key to return to"
def edit_session():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter NAME:")
    nm=input("Enter Correct SESSION:")
    st="update STUDENTS_DATA set Session='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_name():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter NAME:")
    nm=input("Enter Correct NAME:")
    st="update STUDENTS_DATA set SName='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_class():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter NAME:")
    nm=input("Enter Correct CLASS:")
    st="update STUDENTS_DATA set SClass='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_section():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.section()
    ac=input("Enter NAME:")
    nm=input("Enter Correct SECTION:")
    st="update STUDENTS_DATA set SSection='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_rollno():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter NAME:")
    nm=input("Enter Correct ROLL NO.:")
    st="update STUDENTS_DATA set SRollNo='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_sub1():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.sub1()
    ac=input("Enter NAME:")
    nm=input("Enter Correct SUBJECT 1:")
    st="update STUDENTS_DATA set Subject1='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_sub2():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.sub2()
    ac=input("Enter NAME:")
    nm=input("Enter Correct SUBJECT 2:")
    st="update STUDENTS_DATA set Subject2='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_sub3():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.sub3()
    ac=input("Enter NAME:")
    nm=input("Enter Correct SUBJECT 3:")
    st="update STUDENTS_DATA set Subject3='%s' where SName='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
