# SOURCE CODE FOR ADMISSION MENU.
import ADMISSION
import mysql.connector
def ADM_MENU():
    while True:
        print("\t\t...............................................................")
        print("\t\t*******WELCOME TO STUDENT MANAGEMENT SYSTEM*******")
        print("\t\t...............................................................")
        print("\n\t\t*******ADMISSION*******")
        print("1: Admission Details")
        print("2: Show Admission Details")
        print("3: Search")
        print("4: Deletion of Records")
        print("5: Update Admission Details")
        print("6: Return")
        print("\t\t...............................................................")
        choice=int(input("Enter your choice: "))
        if choice==1:
            ADMISSION.Admin_Details()
        elif choice==2:
            ADMISSION.Show_Admin_Details()
        elif choice==3:
            ADMISSION.Search_Admin_Details()
        elif choice==4:
            ADMISSION.Delete_Admin_Details()
        elif choice==5:
            ADMISSION.Edit_Admin_Details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice ...Try Again...")
            conti="Press any key to Return to MAIN_MENU: "
def Admin_Details():
    while True:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="1234",
                                    database="STUDENT_MANAGEMENT")
        cursor=con.cursor()
        adno=input("Enter Admission Number:")
        rno=int(input("Enter RollNo:"))
        sname=input("Enter Student Name:")
        address=input("Enter Address:")
        phone=input("Enter Phone Number.:")
        std=input("Enter Class:")
        query="insert into ADMISSION values('{}',{},'{}','{}','{}','{}')".format(adno,rno,sname,address,phone,std)
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        print("CONGRATS! DESIRED RECORDS HAVE BEEN SAVED IN ADMISSION TABLE")
        print("THANK YOU!...")
        ch=input("Do you want to enter more records?(y/n)")
        if ch=="n":
           break
def Show_Admin_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    cursor.execute("select * from ADMISSION")
    data=cursor.fetchall()
    for row in data:
        print(row)
def Search_Admin_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter admission number:")
    st="Select * from ADMISSION where AdminNo='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print("THANK YOU!...YOUR DESIRED DATA IS...")
    print(data)
def Delete_Admin_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter Admission Number:")
    st="Delete from ADMISSION where AdminNo='%s'"%(ac)
    cursor.execute(st)
    con.commit()
    print("Data deleted successfully")
    print("THANK YOU!")
def Edit_Admin_Details():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    print("1. Edit Name")
    print("2. Edit Address")
    print("3. Phone Number")
    print("4. Return")
    print("\t\t- - - - - - - - - - - - - - -")
    choice=int(input("Enter your choice:"))
    if choice==1:
        ADMISSION.edit_name()
    elif choice==2:
        ADMISSION.edit_address()
    elif choice==3:
        ADMISSION.edit_phno()
    elif choice==4:
        return
    else:
        print("Error:   Invalid choice try again.......")
        conti="press any key to return to"
def edit_name():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter Correct Name:")
    st="update ADMISSION set SName='%s' where AdminNo='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_address():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter Correct Address:")
    st="update ADMISSION set Address='%s' where AdminNo='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
def edit_phno():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database="STUDENT_MANAGEMENT")
    cursor=con.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter Correct PhNo.:")
    st="update ADMISSION set Phone='%s' where AdminNo='%s'"%(nm,ac)
    cursor.execute(st)
    con.commit()
    print("DATA UPDATED SUCCESSFULLY")
    print("THANK YOU!...")
