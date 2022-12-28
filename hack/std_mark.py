n = int(input())
std_mark = {}

for i in range(n):
    name = input()
    line = map(float,input().split())
    mark = list(line)
    std_mark[name] = mark
qname = input()
marks = sum(std_mark[qname])/len(std_mark[qname])
print(marks)


'''Krishna 67 68 69
Arjun 
Malika 52 56 60
Malika'''