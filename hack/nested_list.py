score_list = []
total_list = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list += [[name,score]]
    total_list += [score]
x = sorted(set(total_list))[1]
for n,s in sorted(score_list):
    if s == x:
        print(n)