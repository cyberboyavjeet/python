a=int(input("Enter the no of row required in pattern= "))
#for x in range(1,11):print(x*a)

#nested for loop
for i in range(0,a+1,1):
    for j in range(0,a-i,1):
        print("*",end=" ")
    print(" ")
else : print("Pattren print succesffuly")