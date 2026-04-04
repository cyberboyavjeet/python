with open('demo.txt','w') as file:
    file.write('Hello\nAvjeet\nKumar')
    file.close()
with open('demo.txt','r') as file:
    b=file.readlines()
print(type(b))