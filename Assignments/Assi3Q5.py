def Srt(str):
    lcase=0
    ucase=0
    for i in str:
        if (i.isupper()):
            lcase +=1
        if(i.islower()):
            ucase +=1
    print("Lower letters are: ",ucase)
    print("Upper letter are: ",lcase)
str='Arti is not mine'
Srt(str)