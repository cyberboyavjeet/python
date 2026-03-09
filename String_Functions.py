a=input("Enter the Any String: ")
alph=False
alnumm= False
digit=False

#print(str.expandtabs)
for ch in a:
    if ch.isalpha():
        alph=True
print(alph) 
for ch in a:
    if ch.isalnum():
        alnumm=True
print(alnumm)
for ch in a:
    if ch.isdigit():
    
        digit=True
print(digit)
print(a.isidentifier())
print(a.format())
#print(a.format_map())
print(a.replace("A","AA"))





