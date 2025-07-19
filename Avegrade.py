while True:

    a = input("Enter Name of Student:")
    b = input("Enter Prelim Grade:")
    c = input("Enter Midterm Grade:")
    d = input("Enter Final Grade:")
    e = (int(b) + int(c) + int(d))
    f = e/3
    print("The average grade is", + f)
    if int(f) in range (90, 95):
        print(a + " has passed the semester with honors")
        
    elif int(f) in range (95, 98):
        print(a + " has passed the semester with high honors")
        
    elif int(f) in range (98, 100):
        print(a + " has passed the semester with highest honors")

    elif int(f) in range (75, 90):
        print(a + " has passed the semester")

    else:
        print(a + " has failed the semester")

    while True:
        g = input("Input another average? Pls type yes/no:")
        if g == "yes":
            break
        elif g == "no":
            h = str(input("Thank you for using python!"))
            print(h)
            exit()
            break
        else:
            print("Syntax Error")
            continue
