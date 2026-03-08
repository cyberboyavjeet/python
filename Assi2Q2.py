print("         Even Number Generator Script      ")
print("                                            ")
a=int(input("Enter the Starting Range: "))
b=int(input("Enter the Ending Range: "))
for i in range(a,b+1):
    if(i%2!=0):
        continue
    print(i)