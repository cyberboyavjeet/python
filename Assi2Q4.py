a=int(input("Enter the number: "))
sum=0
while(a%10!=0):
    
    sum =sum+(a%10)
    a=a//10
print(sum)