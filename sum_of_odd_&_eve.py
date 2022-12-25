def odd(i,j):
    sum = 0
    sum1 = 0
    for i in range (1,50):
        if i%2 != 0:
            sum = sum + i
    print("sum of odd",sum)
    for j in range(1,50):
        if j%2 == 0:
            sum1 = sum1 + j
    print("sum of even",sum1)
odd(0,0)

def eve(start,end):
    sum2 = 0
    sum3 = 0
    while start <= end:
        if start%2 == 0:
            sum2 = sum2 + start
        if start%2 != 0:
            sum3 = sum3 + start
        start = start + 1
    print("sum of eve:",sum2)
    print("sum of odd:",sum3)
eve(1,50)