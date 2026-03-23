n=int(input("Enter the Np of rows: "))
# Upper half (including middle)
for i in range(1, n + 1):
    if i == 1:
        print(' ' * (n - i) + '*')
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')

# Lower half
for i in range(n - 1, 0, -1):
    if i == 1:
        print(' ' * (n - i) + '*')
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')