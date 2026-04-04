file=open('Intro.txt','w')
file.write('Name: Avjeet Kumar\n')
file.write('College: Unknown')
file.close()
f=open('Intro.txt','r')
for i in f:
    print(i)