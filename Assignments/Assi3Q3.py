def Multi(a):
    mul=1
    for i in a:
        mul *=i
    return mul
a=[]
r=int(input("How MAny Numbers will be In list: "))
for i in range(r):
    num=int(input(f"Enter the {i+1} Number of List: "))
    a.append(num)
print("List is: ",a)
print("Multiplication: ",Multi(a))