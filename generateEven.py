a=int(input("Enter the Starting Range"))
b=int(input("Enter the last range"))
for x in range(a,b):
    if(x%2==0):
        print("Even: ", x)
        