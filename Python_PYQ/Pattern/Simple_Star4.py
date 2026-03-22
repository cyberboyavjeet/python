a=int(input("Enter the No of line: "))
for i in range (0,a):
    for j in range(0,i+1):
        print((chr(65+j)),end=" ")
        
    print()