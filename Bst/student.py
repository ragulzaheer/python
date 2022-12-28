def student():
    Student = []
    for i in range(1,4):
        Student = open(str(i)+"std.txt","w")
    Name = input("Enter Name:")
    Roll_Number = int(input("Enter Roll Number:"))
    Class = int(input("Enter class:"))
    School = input("Enter school Name:")
    sub1 = int(input("Tamil:"))
    sub2 = int(input("English:"))
    sub3 = int(input("Math:"))
    sub4 = int(input("Scince:"))
    sub5 = int(input("S.S:"))
    Total = sub1 + sub2 + sub3 + sub4 + sub5
    Percent = (Total/500)*(100) 
    
    Student = open("1std.txt","w")
    Student.write("Name :"+str(Name))
    Student.write("\nRoll Number : "+str(Roll_Number))
    Student.write("\nClass : "+str(Class))
    Student.write("\nSchool Name : "+str(School))
    
    Student.writelines("Tamil="+str(sub1)+"\n")
    Student.writelines("English="+str(sub2)+"\n")
    Student.writelines("Math="+str(sub3)+"\n")
    Student.writelines("Scince="+str(sub4)+"\n")
    Student.writelines("S.S="+str(sub5)+"\n")
    Student.writelines("Total="+str(Total)+"\n")
    Student.write("Percentage="+str(Percent)+"%"+"\n")
    if sub1 < 35:
        Student.write("Fail")
    
    elif sub2 < 35:
        Student.write("Fail")

    elif sub3 < 35:
        Student.write("Fail")

    elif sub4 < 35:
        Student.write("Fail")
        
    elif sub5 < 35:
        Student.write("Fail")
    
    else:
        Student.write("Pass")
    
    Name1 = input("Enter Name:")
    Roll_Number1 = int(input("Enter Roll Number:"))
    Class1 = int(input("Enter class:"))
    School1 = input("Enter school Name:")
    sub1_1 = int(input("Tamil:"))
    sub2_1 = int(input("English:"))
    sub3_1 = int(input("Math:"))
    sub4_1 = int(input("Scince:"))
    sub5_1 = int(input("S.S:"))
    Total = sub1_1 + sub2_1 + sub3_1 + sub4_1 + sub5_1
    Percent = (Total/500)*(100)
    
    Student = open("2std.txt","w")
    Student.write("Name :"+str(Name1))
    Student.write("\nRoll Number : "+str(Roll_Number1))
    Student.write("\nClass : "+str(Class1))
    Student.write("\nSchool Name : "+str(School1))

    Student.writelines("Tamil="+str(sub1_1)+"\n")
    Student.writelines("English="+str(sub2_1)+"\n")
    Student.writelines("Math="+str(sub3_1)+"\n")
    Student.writelines("Scince="+str(sub4_1)+"\n")
    Student.writelines("S.S="+str(sub5_1)+"\n")
    Student.writelines("Total="+str(Total)+"\n")
    Student.write("Percentage="+str(Percent)+"%"+"\n")
    if sub1_1 < 35:
        Student.write("Fail")
    
    elif sub2_1 < 35:
        Student.write("Fail")

    elif sub3_1 < 35:
        Student.write("Fail")

    elif sub4_1 < 35:
        Student.write("Fail")
        
    elif sub5_1 < 35:
        Student.write("Fail")
    
    else:
        Student.write("Pass")
    
    Name2 = input("Enter Name:")
    Roll_Number2 = int(input("Enter Roll Number:"))
    Class2 = int(input("Enter class:"))
    School2 = input("Enter school Name:")
    sub1_2 = int(input("Tamil:"))
    sub2_2 = int(input("English:"))
    sub3_2 = int(input("Math:"))
    sub4_2 = int(input("Scince:"))
    sub5_2 = int(input("S.S:"))
    Total = sub1_2 + sub2_2 + sub3_2 + sub4_2 + sub5_2
    Percent = (Total/500)*(100)
        
    Student = open("3std.txt","w")
    Student.write("Name :"+str(Name2))
    Student.write("\nRoll Number : "+str(Roll_Number2))
    Student.write("\nClass : "+str(Class2))
    Student.write("\nSchool Name : "+str(School2))
    
    Student.writelines("Tamil="+str(sub1_2)+"\n")
    Student.writelines("English="+str(sub2_2)+"\n")
    Student.writelines("Math="+str(sub3_2)+"\n")
    Student.writelines("Scince="+str(sub4_2)+"\n")
    Student.writelines("S.S="+str(sub5_2)+"\n")
    Student.writelines("Total="+str(Total)+"\n")
    Student.write("Percentage="+str(Percent)+"%"+"\n")
    if sub1_2 < 35:
        Student.write("Fail")
    
    elif sub2_2 < 35:
        Student.write("Fail")

    elif sub3_2 < 35:
        Student.write("Fail")

    elif sub4_2 < 35:
        Student.write("Fail")
        
    elif sub5_2 < 35:
        Student.write("Fail")
    
    else:
        Student.write("Pass")
    
student()