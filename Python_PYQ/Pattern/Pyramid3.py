n = int(input("Enter the No of lines: "))
for i in range(1, n+1):
    nums = ""
    for j in range(1, 2*i):
        nums += str(j)
    print(" " * (n-i) + nums)