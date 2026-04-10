def Sum(a):
    s=0
    for i in a:
        s +=i
    return s
a=[]
n=int(input("How many Number are there: "))
for i in range(n):
    num=int(input(f"Enter the {i+1} Number: "))
    a.append(num)
print("List is: ",a)
print("Sum: ",Sum(a))