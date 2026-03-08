#Atm verification
cn=int(input("Enter the Card Number: "))
pn=int(input("Enter your Atm pin: "))
while True:
    print("                   ")
    print("                          Welcome to ATM Features                   ")
    print("                                                                     ")
    print("1: Account balance Enquiry                            2:  know your Mobile Number")
    print("3: Know Your Email id                                 4:  Know Your Details ")
    print("5: Exit")
    ch=int(input("Enter the your chioce: "))
    if ch==1 :
        print("Acc. No: xxxxxxxxxxx1265")
        print("Balace: 0.00")
    if ch==2:
        print("Acc. No: xxxxxxxxxxx1265")
        print("Mobile No: xxxxxxx50")
    if ch==3:
        print("Email id: xxxxxxti@gmail.com")
    if ch==4:
        print("Acc. No:          xxxxxxxxxx1265")
        print("IFSC code:        xxxxxxxxCHH")
        print("Acc. Holder Name: Axxx Kxxxx")
        print("Modile No:        xxxxxxx50")
        print("Bank Name:        Airtel Payment bank ")
    if ch==5:
        print("                                      ")
        print("                                ThankYou for using!                     ")
        print("                   ")
        print("Please Remove Your Card")
        break
