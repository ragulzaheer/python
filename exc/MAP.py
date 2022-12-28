def fun(n):
    return n+n
numbers = (1,2,3,4,5)
Ans = map(fun,numbers)
print(list(Ans))

if __name__ == '__main__':
    n = int(input().strip())
if n%2 != 0:
    print("Weird")
elif n%2 == 0 in range(2,5):
    print("Not Weird")
elif n%2 == 0 and n>6 and n<=20:
    print("Weird")
elif n%2 == 0 :
    n > 20
    print("Not Weird")


b = int(input())
a =list(map(int,input()))
x = 0
y = 0
z = 0
for i in range (0,len(a)):
    
    if i >a[i]:
        x = x+1
    elif i <a[i]:
        y = y+1
    else :
        z = z+1
    print(x/len(a))
    print(y/len(a))
    print(z/len(a))

