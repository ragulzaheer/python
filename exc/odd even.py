def odd(i,j):
    for i in range (1,10):
        if i%2 != 0:
            print("odd",i)
    for j in range(1,10):
        if j%2 == 0:
            print("even",j)
odd(0,0)

#start = int(input("num"))
def eve(start,end):
    #i = start
    while start <= end:
        if start%2 == 0:
            print("whe",start)
        
        start = start+1
        if start%2 != 0:
            print("who",end)
    #start = start+1
eve(10,20)

'''def ODD(num):
    while num<=20:
        print(num)
       num = num+2
ODD(1)'''

    