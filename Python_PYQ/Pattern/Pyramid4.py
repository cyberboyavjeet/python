n = int(input("Enter the No of lines: "))
for i in range(1, n+1):
    nums = ""
    for j in range(1, i+1):         # count up: 1 2 3
        nums += str(j)
    for j in range(i-1, 0, -1):     # count down: 2 1
        nums += str(j)
    print(" " * (n-i) + nums)