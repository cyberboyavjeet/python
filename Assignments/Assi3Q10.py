def Perfect(n):
    divisor=0
    if n<1:
        return "No"
    else: 
        for i in range(1,n):
            if(n%i==0):
                divisor +=i

    if(divisor==n):
        return 'Yes'
    else: 
        return 'No'
n=int(input("Enter the Number to be Checked: "))
print(f"Number {n} is :",Perfect(n))
