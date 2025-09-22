def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if(b==0):
        print("can not divide by 0")
    else:
        return a/b
choice='y'
while(choice!='n'):
    print("1.Addition(+)\n2.Subtraction(-)\n3.Mutiplication(x)\nDivision(/)\n")
    ch=int(input("Enter your choice..(eg.1 for addition and so on) "))
    if(ch==1):
        num1=int(input("Enter 1st Number: "))
        num2=int(input("Enter 2nd Number: "))
        print(add(num1,num2))
    elif(ch==2):
        num1=int(input("Enter 1st Number: "))
        num2=int(input("Enter 2nd Number: "))
        print(subtract(num1,num2))
    elif(ch==3):
        num1=int(input("Enter 1st Number: "))
        num2=int(input("Enter 2nd Number: "))
        print(multiply(num1,num2))
    elif(ch==4):
        num1=int(input("Enter 1st Number: "))
        num2=int(input("Enter 2nd Number: "))
        print(divide(num1,num2))
    
    choice=input("Do you want to Continue(y) or Exit(n)? ").lower()


        