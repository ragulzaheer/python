'''num = int(input("num:"))
i = 2
prime = True
while i < num:
    if (num%i == 0):
        print("not prime")
        prime = False
        break
    i = i+1
    if prime:
        print("prime")
        break'''

def prime(start,end):
    for number in range(start,end+1):
        if number > 1:
            for i in range(2,number):
                if number%i == 0:
                    break
            else:
                print(number)

prime(1,10)



        
