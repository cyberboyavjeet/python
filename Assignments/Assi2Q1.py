a=int(input("Enter the first Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Third Number: "))
if(a>b):
    if(a>c):
        print("Greatest Number : ",a)
    else:print("Greatest Number: ",c)
elif(b>a):
    if(b>c):
        print("Greatest NUmber: ",b)
    else:print("Greatest Number: ",c)