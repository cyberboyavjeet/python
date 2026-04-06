f=open("Gaurav.txt","w")
f.write("Avjeet The Don\n Ch\n")
f.close()

f=open("Gaurav.txt",'r')
#f.seek(2)
#print(f.tell())
print(f.readline(2))
#print("❤")