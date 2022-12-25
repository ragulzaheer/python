def student():
    def student_details():
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

    Student = []
    for i in range(1,11):
        Student = open(str(i)+"STD.txt","w")
    Student = open("1STD.txt","w")
    student_details()
    Student = open("2STD.txt","w")
    student_details()
    Student = open("3STD.txt","w")
    student_details()
    Student = open("4STD.txt","w")
    student_details()
    Student = open("5STD.txt","w")
    student_details()
    Student = open("6STD.txt","w")
    student_details()
    Student = open("7STD.txt","w")
    student_details()
    Student = open("8STD.txt","w")
    student_details()
    Student = open("9STD.txt","w")
    student_details()
    Student = open("10STD.txt","w")
    student_details()

student()