def add(a,b):
    c = a + b
    print(c)
def sub(a,b):
    c = a - b
    print(c)
def mul(a,b):
    c = a * b
    print(c)
def div(a,b):
    c = a/  b
    print(c)
def name(a,b):
    Name = a + " " +b
    print(Name)
add(5,3)
sub(5,5)
mul(5,5)
div(5,5)
name("Ragul","Gunasekaran")

list = [1,2,3,4,5]
add_list = list[0] + list[1] + list[2] + list[3] + list[4]
print(add_list)

def addition(list):
    total = 0    
    for i in range (0,len(list)):
        total = total + list[i] 

    print(total)

addition([0,1,2,3])

def ADD(list3):
    total = 0
    i = 0
    #list = [0,1,2]
    while i < len(list3):
        total = total +list3[i]
        i += 1
    print(total)
ADD([1,2,3,4,5])
   
list = [0,1,2]
total = sum(list)
print(total)


'''n = int(input())
for i in range(0,n):
    i = i*i
    print(i)'''



def is_leap(year):
    #year = int(input())
    if year%400 ==0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    
    else:
        return False
     
        
        
year = int(input())
print(is_leap(year))

n = int(input())
for i in range(1,n+1):
    print(i,end="")
