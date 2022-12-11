#SOURCE CODE FOR MAIN MENU.
import MAIN_MENU
import ADMISSION
import STUDENTS_DATA
while True:
    print("\t\t...............................................................")
    print("\t\t*******WELCOME TO STUDENT MANAGEMENT SYSTEM*******")
    print("\t\t...............................................................")
    print("\n\t\t**********ABC PUBLIC SCHOOL************")
    print("1: ADMISSION")
    print("2: STUDENTS_DATA")
    print("3: EXIT")
    print("\t\t---------------------------------------------------------------")
    choice=int(input("Enter your choice: "))
    if choice==1:
        ADMISSION.ADM_MENU()
    elif choice==2:
        STUDENTS_DATA.STU_MENU()
    elif choice==3:
        break
    else:
        print("Error: Invalid Choice ...Try Again...")
        conti=input("Press any key to continue: ")
