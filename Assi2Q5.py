a=int(input("Enter the Number to be reveresed: "))
rev=0
#b=a
dig=0
while(a%10!=0):
    dig=a%10
    rev=rev*10+dig
    a=a//10

#if(b==rev):
   # print("pallindrom")
print(rev)
