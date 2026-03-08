string =input("Enter the pattern like a2b3: ")
result=""
if x in range(0,len(string),2):
    ch=string[x]
    num=int(string[x+1])
    result+=ch*num
print(result)