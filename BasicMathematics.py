a=int(input("Enter the first Number: "))
b=int(input("Enter the Second Number: "))
while True:
    print("                       ")
    print("==========chioce=======")
    print("1: Addition")
    print("2: Subtration")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")
    chioce=int(input("Enter the chioce: "))
    if chioce==1:
        print("Addition= ", a+b)
    if chioce==2:
        print("Subtraction= ",a-b)
    if chioce==3:
        print("Multiplication= ",a*b)
    if chioce==4:
        print("Divison= ",a/b)
    if chioce==5:
        print("Thank!")
        break