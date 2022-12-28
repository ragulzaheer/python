def leap_year(year):
    if year%100==0 and year%400 == 0:
        print('This is leap year')
    elif year%4 ==0 and year%100!=0:
        print('This is leap year')
    else:
        print('Not leap year')
leap_year(2024)

def leap(start,end):

    for i in range(start,end+1):
        if i%100==0 and i%400 == 0:
            print(i)
        elif i%4 ==0 and i%100!=0:
            print(i)
leap(1900,2000)

    