def EvenList(li):
    nli=[]
    for i in li:
        if(i%2==0):
          nli.append(i)
    return nli
li=[]
n=int(input("How Many Elements will be in Lists: "))
for i in range(n):
    num=int(input(f"Enter the {i+1} nUmber of list: "))
    li.append(num)
print(EvenList(li))