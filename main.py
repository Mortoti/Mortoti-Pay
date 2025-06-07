from Class_Vault import *
print ("Welcome to Mortoti Pay")
print("1. Create Account")
print("2. Login")
try:
    option = int(input("<< "))
except ValueError:
    print("You were supposed to enter a digit")
if option == 1:
    Mortoti.create_account()
if option == 2:
    if Mortoti.login():
        while True:
                print("What do you want to do today? ")
                print("1. Deposit")
                print("2. Transfer Money")
                print("3. Withdraw Cash")
                print("4. Purchase Airtime")
                print("5. Check Balance")
                print("6. Change PIN")
                print("7. Delete Account")
                print("8. Logout")
                try:
                    option = int(input("<< "))
                    if option == 1:
                        Mortoti.deposit()
                    elif option == 2:
                        Mortoti.transfer_money()
                    elif option == 3:
                        Mortoti.withdraw()
                    elif option== 4:
                        Mortoti.airtime()
                    elif option==5:
                        Mortoti.check_balance()
                    elif option ==6:
                        Mortoti.change_pin()
                    elif option==7:
                        Mortoti.delete_account()
                    elif option==8:
                        print("Logging out...")
                        exit()
                    else:
                        print("Invalid Option")
                        
                except ValueError:
                     print("You were supposed to enter a digit")

