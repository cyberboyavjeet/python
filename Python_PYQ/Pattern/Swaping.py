a=input("Enter the String: ")
b=''
temp=list(a)
A=temp[0]
temp[0]=temp[-1]
temp[-1]=A
print(b.join(temp))