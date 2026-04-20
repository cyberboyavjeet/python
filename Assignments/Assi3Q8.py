def Prime(n):
    for i in range(2,n//2):
        if (n%i==0):
            return 'Not Prime'
        else :
            return 'Prime'
n=int(input("Enter the Number to be Checked: "))
if(n==0 or n==1):
    print(f"Number {n} is Prime")
else: 
   print(f"Number  {n} is: ",Prime(n))
