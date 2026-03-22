a=int(input("Enter the No of line: "))
for i in range (a,0,-1):
    for j in range(0,i):
        print((chr(65+j)),end=" ")
        
    print()