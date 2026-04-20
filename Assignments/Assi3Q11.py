def Pallindrom(str):
    if str==str[::-1]:
        return 'Pallindrom'
    else:
         return 'Not Pallindrom'
str=input("Enter the String to be Checked: ")
print(f"String {str} is ",Pallindrom(str))
