while True:

    x = int (input('1st number: '))

    y = int (input('2nd number: '))

    sign = input ("Select equation (+, -, *, /)")

    a = x + y
    b = x - y
    c = x * y
    d = x / y

    if sign in ('+','-','*','/'):

        if sign == '+':
            print(x, "+", y, "=", str (a))

        elif sign == '-':
            print(x, "-", y, "=", str (b))

        elif sign == '*':
            print(x, "*", y, "=", str (c))

        elif sign == '/':
            print(x, "/", y, "=", str (d))

        while True:
            
            restart = input("Use the calculator again? (y/n): ")
            if restart == "y":
             break
            elif restart == "n":
             e = str(input("Thank you for using this calculator!"))
             print(e)
             exit()
             break
            else:
             print ("Wrong input")


    else:
        print("Syntax Error")