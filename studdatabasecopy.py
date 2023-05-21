print("\t\t----------------------------------------------------------------")
print("\t\t****************************************************************")
print("\n\n\t\t\tSUBTASK 1 FOR CODING CLUB")
print("\n\n\n\t\t\t\tNAME:   YOSHITA    BANERJEE")
print("\n\n\t\t\t\tROLL NUMBER: 220107098")
print("\n\n\t\t****************************************************************")
print("\t\t----------------------------------------------------------------")
print("\t\t\t\tpress any key to cont...")
input()
print("\n\n")

import pickle
import os

#ADDING RECORDS OF STUDENTS

def writeRec():
    fin=open("e:/yoshita/projstud.dat",'rb')
    crec=0
    try:
        while True:
            st=pickle.load(fin)
            attendance=pickle.load(fin)
            lst=st.split(",")
            crec=int(lst[3])
    except EOFError:
        fin.close()
    fout=open("e:/yoshita/projstud.dat",'ab')
    stud=""
    attendance={"JAN":0,"FEB":0,"MAR":0,"APR":0,"MAY":0,"JUN":0,"JUL":0,"AUG":0,"SEP":0,\
               "OCT":0,"NOV":0,"DEC":0}
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print("\t\t\t\tSTUDENT  DATA  ENTRY  SCREEN")
    name=input("\n\n\t\tEnter the name of the student:")
    cl=input("\n\n\t\tEnter the class in roman letters:")
    sec=input("\n\n\t\tEnter the section:")
    address=input("\n\n\t\tEnter the address of the student:")
    regno=crec+1
    stud=name+","+cl+","+sec+","+str(regno)+","+address+"\n"
    pickle.dump(stud,fout)
    pickle.dump(attendance,fout)
    fout.close()

#END OF writeRec()....

#ADDING ATTENDANCE OF A STUDENT

def accept_attendance(reg):
    fin=open("e:/yoshita/projstud.dat",'rb')
    fout=open("e:/yoshita/trans.dat",'wb')
    #print("hello")
    c=0
    try:
        while True:
            #print("hello")
            st=pickle.load(fin)
            attendance=pickle.load(fin)
            c+=1
            l=st.split(",")
            #print(l)
            #print(attendance)
            if reg==int(l[3]):
                #print(attendance)

                mno=input("\n\n\t\tEnter the only first 3 letters of the month name:")
                if attendance[mno]==0 or attendance[mno]>22:

                    atno=int(input("\n\n\t\tEnter the attendance:"))
                    attendance[mno]=atno
                    #print(attendance)
                else:
                    print("\n\n\t\tATTENDANCE FOR THE PARTICULAR MONTH ALREADY EXISTS")
                pickle.dump(st,fout)
                pickle.dump(attendance,fout)
            else:
                pickle.dump(st,fout)
                pickle.dump(attendance,fout)


    except EOFError:
        fin.close()


    if c==0:
        print("\n\n\n\t\t\tTO VIEW RECORDS PLEASE ENTER RECORDS FIRST\n")
    fout.close()
    os.remove("e:/yoshita/projstud.dat")
    os.rename("e:/yoshita/trans.dat","e:/yoshita/projstud.dat")

#END OF accept_attendance()....


#TO DISPLAY THE RECORDS OF STUDENTS

def display(rec,att):
    lst=rec.split(",")
    print("\n\n")
    print("NAME:",lst[0])
    print("CLASS:",lst[1])
    print("SECTION:",lst[2])
    print("REGISTRATION NUMBER:",lst[3])
    print("ADDRESS:",lst[4])
    print("ATTENDANCE:",att)
    print("\n\n\n\t\t\t\tpress any key to cont...")
    input()

#END OF display()....

#VIEWING DETAILED INFORMATION OF STUDENTS

def viewRec():
    fin=open("e:/yoshita/projstud.dat",'rb')
    c=0
    print("\n\n\n\n\n\n\n\n\n\t\t\t\tDETAILED STUDENTS INFORMATION\n")
    try:
        while True:
            st=pickle.load(fin)
            attendance=pickle.load(fin)
            c+=1
            display(st,attendance)
    except EOFError:
        fin.close()
    if c==0:
        print("\n\t\t\t\tTO VIEW RECORDS YOU NEED TO ENTER RECORDS FIRST\n")

#END OF viewRec()....

#VIEWING DETAILS OF A PARTICULAR STUDENT

def viewRec_particular(reg):
    fin=open("e:/yoshita/projstud.dat",'rb')
    flag=0
    c=0
    print("\n\n\n\n\n\n\n\n\n\t\t\t\tDETAILED STUDENTS INFORMATION\n")
    try:
        while True:
            st=pickle.load(fin)
            attendance=pickle.load(fin)
            c+=1
            l=st.split(",")
            if int(l[3])==reg:
                flag=1
                display(st,attendance)
    except EOFError:
        fin.close()
    if c==0:

        print("\n\t\t\t\tTO VIEW RECORDS YOU NEED TO ENTER RECORDS FIRST\n")
    if flag==0:
        print("REGISTRATION NO. NOT MATCHED")

#END OF viewRec_particular()....

#VIEWING THE ATTENDANCE OF A STUDENT

def viewAttendance(reg):
    fin=open("e:/yoshita/projstud.dat",'rb')
    flag=0
    c=0
    print("\n\n\n\n\n\n\n\n\n\t\t\t\tDETAILED STUDENTS INFORMATION\n")
    try:
        while True:
            st=pickle.load(fin)
            attendance=pickle.load(fin)
            c+=1
            l=st.split(",")
            if int(l[3])==reg:
                flag=1
                print("\t\t\t\t\tMONTH     ATTENDANCE")
                for key in attendance:
                    print("\t\t\t\t\t",key,"\t\t",attendance[key])
                print("press any key to continue....")
                ch=input()

    except EOFError:
        fin.close()
    if c==0:

        print("\n\t\t\t\tTO VIEW RECORDS YOU NEED TO ENTER RECORDS FIRST\n")
    if flag==0:
        print("REGISTRATION NO. NOT MATCHED")

#END OF viewAttendance()....

#DELETING RECORDS OF A PARTICULAR STUDENT

def delRec(regno):
    fin=open("e:/yoshita/projstud.dat",'rb')
    fout=open("e:/yoshita/trans.dat",'wb')
    flag=0
    #TO CATCH ANY EXCEPTIONS
    try:
        while True:
            st=pickle.load(fin)
            attendance=pickle.load(fin)
            lst=st.split(",")
            if int(lst[3])!=regno:
                #print("hello")
                pickle.dump(st,fout)
                pickle.dump(attendance,fout)
            elif int(lst[3])==regno:
                flag=1
                print("\n\n\n\n\n\nTHIS PARTICULAR RECORD WILL BE DELETED")
                display(st,attendance)



    except EOFError:
        fin.close()
    if flag==0:
        print("\n\n\n\nREGISTRATION NUMBER TO BE DELETED DOES NOT EXIST")
    fout.close()
    os.remove("e:/yoshita/projstud.dat")
    os.rename("e:/yoshita/trans.dat","e:/yoshita/projstud.dat")

#END OF delRec()....

#*************MAINMENU***************

fout=open("e:/yoshita/projstud.dat",'ab')
fout.close()
#PROVIDING THE USER WITH OPTIONS FOR PERFORMING SPECIFIC TASKS
choice=1
while choice:
    print("\t\t\t\t________________________")
    print("\n\n\n\t\t\t\t\tMAIN MENU")
    print("\n\n\n\t\t\t\t________________________")
    print("\n\n\n\t\t\t\t1:ADDING A RECORD TO A DATABASE")
    print("\t\t\t\t2:VIEWING RECORDS")
    print("\t\t\t\t3:DELETING A RECORD")
    print("\t\t\t\t4:ADDING ATTENDANCE OF A STUDENT")
    print("\t\t\t\t5:MODIFYING A RECORD")
    print("\t\t\t\t6:EXIT")
    choice=int(input("\n\t\t\t\tEnter user's choice:"))
    if choice==1:
        writeRec()

    elif choice==2:
       while True:
            print("\n\n\n\n\n\n\t\t\tSUB  MENU  FOR  VIEWING  RECORDS")
            print("\t\t\t_________________________________")
            print("\n\n\t\t\t\ta:VIEWING ALL STUDENTS' RECORDS")
            print("\t\t\t\tb:VIEWING DETAILS INFO OF PATICULAR STUDENT")
            print("\t\t\t\tc:VIEWING ATTENDANCE DETAILS OF A PARTICULAR STUDENT")
            print("\t\t\t\td:GO BACK TO MAIN MENU")
            ch=input("\n\n\t\t\t\tEnter your choice (a,b,c,d):")
            if ch in ["a","A"]:
                 viewRec()
            elif ch in ["b","B"]:
                print("\n\n\n\n\n\n\n\n\n\n")
                r=int(input("\t\tEnter the registration number of the student:"))
                viewRec_particular(r)
            elif ch in ["c","C"]:
                print("\n\n\n\n\n\n\n\n\n\n")
                r=int(input("\t\tEnter the registration number of the student:"))
                viewAttendance(r)
            elif ch in ["d","D"]:
                break
            else:
                print("wrong input")

    elif choice==3:
        print("\n\n\n\n\n\n\n\n\n\n")
        r=int(input("\t\tEnter the registration number of the student to be deleted:"))
        delRec(r)

    elif choice==4:
        print("\n\n\n\n\n\n\n\n\n\n")
        r=int(input("\t\tEnter the registration number of the student:"))
        accept_attendance(r)

    elif choice==5:
        print("\n\n\n\n\n\n\n\n\n\n")
        r=int(input("\tEnter the registration number of the student whose record is to be modified:"))
        modifyRec(r)

    elif choice==6:
        break

    else:
        print("INVALID CHOICE")

#END OF *************MAIN**************
