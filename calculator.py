print("Simple Calculator")
while(True):
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    oper = str(input("Enter the operation: +,-,*,/:  "))
    result = None
    if (oper == "+"):
        result = num1+num2
    elif (oper == "-"):
        result = num1-num2
    elif (oper == "*"):
        result = num1*num2
    elif (oper == "/"):
        if (num2==0):
            print("Wrong operation")
        else:
            result = num1/num2
    else:
        print("INVALID CHOICE !!! ENTER THE CORRECT OPERATION: +,-,*,/")
        result = None
    print("Result= ", result)
