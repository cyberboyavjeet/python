a=int(input("enter the number: "))
if(a<=1 ):
    print("Number is not Prime")
    count=0

for i in range(2,a):
    if(a%i==0):
        count=1
if count==1:
    print("Number is not prime")
else:print("Number is Prime")