f=open("Assignment.txt",'w')
f.write("This is Assignment\n Unit 4 is going on\n")
f.close()

l=[]
f=open("Assignment.txt",'r')
for i in range (0,2):
    l.append(f.readline())
print(l)
f.close()
