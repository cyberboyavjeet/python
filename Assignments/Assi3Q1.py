def Max(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else :
          return c
    elif(b>c):
        return b
    else :
        return c
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Third Number: "))
print("MAx:",Max(a,b,c))