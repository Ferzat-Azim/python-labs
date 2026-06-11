while True:


    num1=input("num 1 (or q to quit) : ")
    if num1=="q":
        break
    num1=float(num1)
    num2=float(input("num 2 : "))
    op=input("op( + , - , * , / ):")



    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 / num2)
    else:
        print("Invalid operator")