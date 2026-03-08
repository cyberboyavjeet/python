import string

password = input("Enter a password: ")

upper = False
lower = False
digit = False
symbol = False

if len(password) >= 8:
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch in string.punctuation:
            symbol = True

    if upper and lower and digit and symbol:
        print("Strong Password ")
    else:
        print("Password is not strong ")
else:
    print("Password must be at least 8 characters long ")