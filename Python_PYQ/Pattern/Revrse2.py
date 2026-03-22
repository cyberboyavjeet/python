a=int(input("Enter the Number of Line required in pattern: "))
m=1
for i in range (a,0,-1):
    for j in range(0,i):
        print(m,end=" ")
        m=m+1
        
    print()