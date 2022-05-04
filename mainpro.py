print("Login as:-")
print("\n1.Administrator")
print("2.Student")
pu=input("\nEnter your choise(1/2):")
if pu=='1':
    pswd=input("\nEnter the password: ")
    if pswd=='admin':
        def add_stu():
            print("!__________!Enter details!____________!")
            import mysql.connector
            dbms=mysql.connector.connect(host='localhost',user='root',password="{}".format(pswd),database='rty')
            ro=int(input("Enter the Roll no.:"))
            na=input("Enter the Name:")
            fa=input("Enter the Father's Name:")
            cl=input("Enter the Class:")
            se=input("Enter the Section of {} Class :".format(cl))
            st=input("Enter the Stream:")
            fep=input("Enter the Paid Fees:")
            pfe=input("Enter the Panding Fees:")
            db=input("Enter the Date of Birth(yyyy-mm-dd):")
            ct=int(input("Enter the Contect No.:"))
            em=input("Enter the E-mail:")
                  
            cur=dbms.cursor()
            s="INSERT INTO student(Rollno,Name,Father_Name,Class,Section,Stream,Paid_Fees,Panding_Fees,Birth_Date,Contact,Email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            b1=(ro,na,fa,cl,se,st,fep,pfe,db,ct,em)
            cur.execute(s,b1)
            dbms.commit()

            print("\n-------***Data is successfully entered***-------")
            return()
                
        def  all_rec():
            import mysql.connector
            dbms=mysql.connector.connect(host='localhost',user='root',password="{}".format(pswd),database='rty')
            cur=dbms.cursor() 
            r="SELECT * from student"
            cur.execute(r)
            result=cur.fetchall()
            print('Total no. of Students in Database:',cur.rowcount)
            for row in result:
                print('\nRoll No.:',row[0])
                print('Student Name:',row[1])
                print("Father's Name:",row[2])
                print('Class:',row[3])
                print('Section:',row[4])
                print('Stream:',row[5])
                print('Fees Paid:',row[6])
                print('Fees Panding:',row[7])
                print('Date of Birth:',row[8])
                print('Contact:',row[9])
                print('Email:',row[10])
            return()
    
            
        def srch_stu():
            import mysql.connector
            dbms=mysql.connector.connect(host='localhost',user='root',password="{}".format(pswd),database='rty')
            fi=int(input("Enter the Rollno. of student:"))
            cur=dbms.cursor() 
            r="SELECT * from student WHERE Rollno = {}".format(fi)
            cur.execute(r)
            result=cur.fetchall()
            for row in result:
                print('\nRoll No.:',row[0])
                print('Student Name:',row[1])
                print("Father's Name:",row[2])
                print('Class:',row[3])
                print('Section:',row[4])
                print('Stream:',row[5])
                print('Fees Paid:',row[6])
                print('Fees Panding:',row[7])
                print('Date of Birth:',row[8])
                print('Contact:',row[9])
                print('Email:',row[10])
            return()
 
        def up_stu():
            import mysql.connector
            dbms=mysql.connector.connect(host='localhost',user='root',password="{}".format(pswd),database='rty')                    
            def up_roll():
                ud=int(input("Enter the Rollno. to Update:"))
                ne=int(input("Enter the New Rollno.:"))
                cur=dbms.cursor()
                s="UPDATE student SET Rollno ={} WHERE Rollno={}".format(ne,ud)
                cur.execute(s)
                dbms.commit()
            return()

            def up_name():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the New Name:"))
                cur=dbms.cursor()
                r="UPDATE student SET Name={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()
                    
            def up_fathername():
                ufp=int(input("Enter the Rollno. to Update:"))
                fna=str(input("Enter the New Father's Name:"))
                cur=dbms.cursor()
                r="UPDATE student SET Father_Name={} WHERE Rollno={}".format(fna,ufp)
                cur.execute(r)
                dbms.commit()
                return()

            def up_class():
                up=int(input("Enter the Class to Update:"))
                na=str(input("Enter the New Class:"))
                cur=dbms.cursor()
                r="UPDATE student SET Class={} WHERE Class={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()

            def up_section():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the New Section:"))
                cur=dbms.cursor()
                r="UPDATE student SET Section={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()
            
            def up_stream():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the New Stream:"))
                cur=dbms.cursor()
                r="UPDATE student SET Stream={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()
    
            def up_Paid():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the Paid Fees:"))
                cur=dbms.cursor()
                r="UPDATE student SET Paid_Fees={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()

            def up_Panding():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the New Stream:"))
                cur=dbms.cursor()
                r="UPDATE student SET Panding_Fees={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()
           
            def up_date():
                up=int(input("Enter the Rollno. to Update:"))
                na=input("Enter the new Date of birth(yyyy-mm-dd):")
                cur=dbms.cursor()
                r="UPDATE student SET Birth_Date={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()

            def up_contact():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the New Contact:"))
                cur=dbms.cursor()
                r="UPDATE student SET Contact={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()
            
            def up_mail():
                up=int(input("Enter the Rollno. to Update:"))
                na=str(input("Enter the New E-mail:"))
                cur=dbms.cursor()
                r="UPDATE student SET Email={} WHERE Rollno={}".format(na,up)
                cur.execute(r)
                dbms.commit()
                return()
    
            def up_all():
                up=int(input("Enter the Rollno. to Update:"))
            
                ne=int(input("Enter the New Rollno.:"))
                cur=dbms.cursor()
                s="UPDATE student SET Rollno ={} WHERE Rollno={}".format(ne,up)
                cur.execute(s)
    
                na=str(input("Enter the New Name:"))
                cur=dbms.cursor()
                r="UPDATE student SET Name={} WHERE Rollno={}".format(na,up)
                cur.execute(r)

                fna=str(input("Enter the New Father's Name:"))
                cur=dbms.cursor()
                t="UPDATE student SET Father_Name={} WHERE Rollno={}".format(fna,up)
                cur.execute(t)

                nc=input("Enter the New Class:")
                cur=dbms.cursor()
                u="UPDATE student SET Class={} WHERE Rollno={}".format(nc,up)
                cur.execute(u)

                ns=input("Enter the New Section:")
                cur=dbms.cursor()
                v="UPDATE student SET Section={} WHERE Rollno={}".format(ns,up)
                cur.execute(v)
    
                nst=str(input("Enter the New Stream:"))
                cur=dbms.cursor()
                w="UPDATE student SET Stream={} WHERE Rollno={}".format(nst,up)
                cur.execute(w)
    
                npf=str(input("Enter the Paid Fees:"))
                cur=dbms.cursor()
                x="UPDATE student SET Paid_Fees={} WHERE Rollno={}".format(npf,up)
                cur.execute(x)
    
                nfp=str(input("Enter the Panding Fees:"))
                cur=dbms.cursor()
                y="UPDATE student SET Panding_Fees={} WHERE Rollno={}".format(nfp,up)
                cur.execute(y)
                
                nd=input("Enter the new Date of birth(yyyy-mm-dd):")
                cur=dbms.cursor()
                z="UPDATE student SET Birth_Date={} WHERE Rollno={}".format(nd,up)
                cur.execute(z)
        
                nco=str(input("Enter the New Contact:"))
                r=dbms.cursor()
                e="UPDATE student SET Contact={} WHERE Rollno={}".format(nco,up)
                cur.execute(e)

                nm=str(input("Enter the New E-mail:"))
                cur=dbms.cursor()
                f="UPDATE student SET Email={} WHERE Rollno={}".format(nm,up)
                cur.execute(f)
                dbms.commit()
                return()
        
            print("1. Roll No.")
            print("2. Name")
            print("3. Father's Name")
            print("4. Class")
            print("5. Section")
            print("6. Stream")
            print("7. Paid Fees")
            print("8. Panding Fees")
            print("9. Date of Birth")
            print("10. Contect")
            print("11. E-mail")
            print("12. All")
            ch=input("Enter your choice:")
            if ch=='1':
                up_roll()
    

            elif ch=='2':
                up_name()
                        
                        
            elif ch=='3':
                up_fathername()

                        
            elif ch=='4':
                up_class()

                        
            elif ch=='5':
                up_section()

                        
            elif ch=='6':
                up_stream()
    

            elif ch=='7':
                up_Paid()


            elif ch=='8':
                up_Panding()


            elif ch=='9':
                up_date()


            elif ch=='10':
                up_contact()
        

            elif ch=='11':
                up_mail()


            elif ch=='12':
                up_all()

         
            else:   
                print("invalid")
                  
            return()

        def del_stu():
            import mysql.connector
            dbms=mysql.connector.connect(host='localhost',user='root',password="{}".format(pswd),database='rty')
            de=int(input("Enter the Roll no. to delete data:"))
            cur=dbms.cursor()
            s="DELETE FROM student WHERE Rollno={}".format(de)
            cur.execute(s)
            dbms.commit()

            print("\nData of Roll No. {} is successfully deleted".format(de))
            return()
                
                    
        while True:
            print("Select operation.")
            print("1. Add New Student")
            print("2. View All Students Data")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Quit")
            choice = input("Enter choice: ")
            print("---*---*---*---*---*---*---*---*---*---*---*---*---")

            if choice in ('1', '2', '3', '4', '5'):
            
                if choice == '1':
                    add_stu()                        
                    f1=input("\nDo you want to continue with this program (y/n):")
                    if f1=='y':
                        continue
                    else:
                        break
                            
                elif choice == '2':
                    all_rec()
                    f1=input("\nDo you want to continue with this program (y/n):")
                    if f1=='y':
                            continue
                    else:       
                            break

                elif choice == '3':
                    srch_stu()
                    f1=input("\nDo you want to continue with this program (y/n):")
                    if f1=='y':
                            continue
                    else:
                            break

                elif choice == '4':
                    up_stu()
                    f1=input("\nDo you want to continue with this program (y/n):")
                    if f1=='y':
                            continue
                    else:
                            break
    
                elif choice == '5':
                    del_stu()
                    f1=input("\nDo you want to continue with this program (y/n):")
                    if f1=='y':
                            continue
                    else:
                            break

                elif choice == '6':
                    break
                  
                else:
                    print("Invalid Choice")

            break
    else:
        print("INVALID PASSWORD")


elif pu=='2':
    def  all_rec():
        import mysql.connector
        dbms=mysql.connector.connect(host='localhost',user='root',password='admin',database='rty')
        cur=dbms.cursor() 
        r="SELECT * from student"
        cur.execute(r)
        result=cur.fetchall()
        print('\nTotal no. of Students in Database:',cur.rowcount)
        for row in result:
            print('\nRoll No.:',row[0])
            print('Student Name:',row[1])
            print("Father's Name:",row[2])
            print('Class:',row[3])
            print('Section:',row[4])
            print('Stream:',row[5])
            print('Fees Paid:',row[6])
            print('Fees Panding:',row[7])
            print('Date of Birth:',row[8])
            print('Contact:',row[9])
            print('Email:',row[10])
        return()

    
    def srch_stu():
        import mysql.connector
        dbms=mysql.connector.connect(host='localhost',user='root',password='admin',database='rty')
        fi=int(input("Enter the Rollno. of student:"))
        cur=dbms.cursor() 
        r="SELECT * from student WHERE Rollno = {}".format(fi)
        cur.execute(r)
        result=cur.fetchall()
        for row in result:
            print('\nRoll No.:',row[0])
            print('Student Name:',row[1])
            print("Father's Name:",row[2])
            print('Class:',row[3])
            print('Section:',row[4])
            print('Stream:',row[5])
            print('Fees Paid:',row[6])
            print('Fees Panding:',row[7])
            print('Date of Birth:',row[8])
            print('Contact:',row[9])
            print('Email:',row[10])
        return()

    print("\n1. Show All Students Details")
    print("2. Search Student Details")
    w=input("\nEnter your choice:")
    if w=='1':
        all_rec()
        
    elif w == '2':
        srch_stu()

    else:
        print("INVALID OPTION!")

    
