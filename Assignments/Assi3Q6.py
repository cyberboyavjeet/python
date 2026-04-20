def IsRange(s,e,z):
    if z in range(s,e):
        return 'Yes'
    else:
         return 'No'
s=int(input("Enter the Starting Range: "))
e=int(input("Enter the Ending Range: "))
z=int(input("Enter the Number to be Checked: "))
print(IsRange(s,e,z))