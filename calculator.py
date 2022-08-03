while True:
    a = int(input("Enter your first number : "))
    b = int(input("Enter your second number: "))

    print("Calculator Menu:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplicatoin")
    print("4. Division")

    choice=int(input("Enter the type of mathematical operation (1/2/3/4):  "))


    if choice==1:
        print (a, "+", b, "=", a+b)
    elif choice==2:
        print(a, "-", b, "=", a-b)
    elif choice==3:
        print(a, "*", b, "=", a*b)
    elif choice==4:
        print(a, "/", b,"=", a/b)
    else:
        print("Invalid Command")
    
    check=input("Do you want to to Quit or star again (Y/N):")
    if check.lower()=="y":
        continue
    print("byee...")
    break
    