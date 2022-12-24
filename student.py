def student():
    sub1 = int(input("Tamil:"))
    sub2 = int(input("English:"))
    sub3 = int(input("Math:"))
    sub4 = int(input("Scince:"))
    sub5 = int(input("S.S:"))
    Total = sub1 + sub2 + sub3 + sub4 + sub5
    Percent = (Total/5)*(100) 
    
    Student = (open("std1.txt","w"))
    Student.write("Name : Abi")
    Student.write("\nRoll Number : 101")
    Student.write("\nClass : X")
    Student.write("\nSchool Name : Zamindar's Hr. sec. school \n")
    
    Student = (open("std1.txt","a"))
    Student.writelines("Tamil="+str(sub1)+"\n")
    Student.writelines("English="+str(sub2)+"\n")
    Student.writelines("Math="+str(sub3)+"\n")
    Student.writelines("Scince="+str(sub4)+"\n")
    Student.writelines("S.S="+str(sub5)+"\n")
    Student.writelines("Total="+str(Total)+"\n")
    Student.write("Percentage"+str(Percent)+"%")
    
student()