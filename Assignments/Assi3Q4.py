def Fact(a):
    if(a==0 or a==1):
        return 1
    else:
        return a*Fact(a-1)
a=int(input("Enter the Number: "))
print("Factorial: ",Fact(a))