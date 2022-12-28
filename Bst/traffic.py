signal1 = ["Red","Yellow","Green"]
signal2 = ["Red","Yellow","Green"]
signal3 = ["Red","Yellow","Green"]
signal4 = ["Red","Yellow","Green"]
#direction = ["East","West","North","South"]

def manual(direction):
    direct = int(input())
    if direct == 0:
        print(signal1[2])
        print(signal2[0],signal3[0],signal4[0])
    if direct == 1:
        print(signal2[2])
        print(signal1[0],signal3[0],signal4[0])
    if direct == 2:
        print(signal3[2])
        print(signal1[0],signal2[0],signal4[0])
    if direct == 3:
        print(signal4[2])
        print(signal1[0],signal2[0],signal3[0])
manual(["East","West","North","South"])
    