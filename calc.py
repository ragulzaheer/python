operation = input("Operation:")
def calc():
    
    def add():
        num1 = int(input("num1="))
        num2 = int(input("num2="))
        Ans = num1 + num2
        print("Ans=",Ans)
    def sub():
        num1 = int(input("num1="))
        num2 = int(input("num2="))
        Ans = num1 - num2
        print("Ans=",Ans)
    def mul():
        num1 = int(input("num1="))
        num2 = int(input("num2="))
        Ans = num1 * num2
        print("Ans=",Ans)
    def div():
        num1 = int(input("num1="))
        num2 = int(input("num2="))
        Ans = num1 / num2
        print("Ans=",Ans)
    def sqrt():
        num1 = int(input("num1="))
        Ans = num1 * 0.5
        print("Ans=",Ans)
    if operation == "+":
        add()
    if operation == "-":
        sub()
    if operation == "*":
        mul()
    if operation == "/":
        div()
    if operation == "sqrt":
        sqrt()
 
calc()

        