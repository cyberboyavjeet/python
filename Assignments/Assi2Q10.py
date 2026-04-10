a=int(input("Enter the Number of time required: "))
if (a==0):
    print("0")
else:
    fab=0
    i=1
    count=0
    while(count<a):
        print(fab,end=" ")
        c=fab+i
        fab=i
        i=c
        count +=1