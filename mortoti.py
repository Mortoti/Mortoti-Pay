import json
import getpass
import hashlib
class Mortoti:
    user_info = {}
    number = {}
    @classmethod
    def save_users(cls):
        try:
            with open("users.json", "r") as file:
                existing_user = json.load(file)
        except FileNotFoundError:
            existing_user= {}
        existing_user.update(cls.user_info)
        with open("users.json", "w") as file:
                        json.dump(existing_user, file)
                    
    @classmethod
    def load_users(cls):
        try:
            with open("users.json", "r") as file:
                cls.user_info = json.load(file)
        except FileNotFoundError:
            cls.user_info={}
    @classmethod
    def number_check(cls, number):
        if number.isdigit() and len(number)== 10 and (number.startswith("090") or number.startswith("095")):
            return True
        else:
            print("Number not registered in our system")
            return False
    @classmethod
    def balance_check(cls, amount, user_number):
        if amount <= cls.user_info[user_number]["balance"]:
            return True
        else:
            return False
    @classmethod
    def hash_pin(cls,pin):
        return hashlib.sha256(pin.encode()).hexdigest()
    @classmethod
    def pin_check(cls, pin):
        if len(pin) == 4 and pin.isdigit():
            return True
        else:
            print("Invalid PIN")
            return False
    @classmethod
    def create_account(cls):
        
        print("Enter your number: ")
        number = input() 
        if number in cls.user_info:
            print("Account exists already")
        else:
            if cls.number_check(number): 
                user_number = number   
                print("Enter your pin: ")
                pin = getpass.getpass()
                if cls.pin_check(pin):
                    hashed_pin = cls.hash_pin(pin)
                    balance = 0
                    cls.user_info[user_number]= {"pin": hashed_pin, "balance": balance}
                    print("Account Created Successfully")
                    cls.save_users()
                    
            else:
                print("Invalid Number")
                print("Mortoti Pay numbers either starts with 090 or 095")
                return
    @classmethod
    def pin_validation(cls,user_number):
        pin_attempts = 0
        while pin_attempts < 3:
            print("Enter your PIN")
            pin = getpass.getpass("<< ")
            pin_attempts += 1
            if cls.pin_check(pin):
                hashed_pin = cls.hash_pin(pin)
                if hashed_pin == cls.user_info[user_number]["pin"]:
                    return True
                else:
                    print("Invalid PIN")
                    print("Try again")
                    
            
        return False
    
                
    @classmethod
    def login(cls):
        cls.load_users()
        print("Enter your number: ")
        user_number = input("<< ")
        if user_number in cls.user_info:
            if cls.pin_validation(user_number):
                print("Login Successful")
                cls.number= {'user_number': user_number}
                return True
            else:
                print("Login Failed")
                return False
        else:
            print("Account not found")
    @classmethod
    def deposit (cls):
        try:
            print("Enter your deposit amount")
            amount = int(input("<< "))
            user_number = cls.number['user_number']
        except ValueError:
            print("Please enter a digit!")
            return
        
        if amount > 0 :
            if cls.pin_validation(user_number):
                cls.user_info[user_number]["balance"] += amount
                cls.save_users()
                print(f'You have successfully deposited an amount of GHS {amount}. Your account balance is now GHS {cls.user_info[user_number]["balance"]}')
            else:
                print("Incorrect PIN")
                return
        else:
            print("Amount must be greater than 0")
            return
    @classmethod
    def withdraw(cls):
        print("Enter the amount you want to withdraw: ")
        try:
            amount = int(input("<< "))
            user_number = cls.number['user_number']
        except ValueError:
            print("Please enter a digit")
            return       
        if cls.balance_check(amount, user_number):
            if cls.pin_validation(user_number):
                cls.user_info[user_number]["balance"] -= amount
                cls.save_users()
                print(f"You have successfully withdrew GHS {amount}. Your new balance is GHS {cls.user_info[user_number]["balance"]}")
            else:
                    print("Incorrect PIN")
                    return
        else:
                print("Insufficient Balance")
                return
    @classmethod
    def change_pin(cls):
        
        user_number = cls.number['user_number']
        if cls.pin_validation(user_number):
            print("Enter New PIN")
            pin = getpass.getpass("<< ")
            if cls.pin_check(pin):
                hashed_pin = cls.hash_pin(pin)
                cls.user_info[user_number]["pin"] = hashed_pin
                print("PIN changed successfully")
                cls.save_users()
            else:
                print("Invalid PIN")
                return
        else:
            print("Incorrect PIN")
            return
    @classmethod
    def charges(cls, amount):
        if amount <100 :
            charge = 0.5
            amount += charge
            return amount , charge
        else:
            charge = amount / 100
            amount += charge
            return amount , charge
    @classmethod
    def transfer_money(cls):
        
        print("Enter the number you want to transfer money to")
        number = input("<< ")
        user_number = cls.number['user_number']
        if cls.number_check(number) and number!=user_number:
            print("Enter the amount you want to send")
            try:
                amount = int(input("<< "))
                if cls.balance_check(amount, user_number):   
                    if number in cls.user_info:
                        if cls.pin_validation(user_number):
                            amount , charge = cls.charges(amount)
                            cls.user_info[user_number]["balance"] -= amount
                            cls.user_info[number]["balance"] += amount-charge
                            cls.save_users()
                            
                            print(f"You have transferred an amount of GHS {amount-charge} to {number}. You were charged {charge}. Your new balance is {cls.user_info[user_number]["balance"]}")
                        else:
                            print("Incorrect PIN")
                            return
                    else:
                        print("Number not found")
                        return
                else:
                    print("Insufficient balance")
                    return
            except ValueError:
                print("Please enter a digit")
                return
    @classmethod
    def airtime(cls):
        print("1. Self")
        print("2. Others")
        try:
            option = int(input("<< "))
        except ValueError:
            print("You were supposed to enter a digit")
            return
        if option == 1:
            user_number = cls.number["user_number"]
            print("Enter amount")
            try:
                amount = int(input("<< "))
                user_number = cls.number['user_number']
            except ValueError:
                        print("You were supposed to enter a digit")
                        return
            if cls.balance_check(amount, user_number):  
                
                if cls.pin_validation(user_number):
                    cls.user_info[user_number]["balance"] -= amount
                    print(f"You have sucessfully purchased an airtime of GHS {amount}. Your new balance is {cls.user_info[user_number]["balance"]}")
                else:
                    print("Incorrect PIN")
                    return
            else:
                print("Insufficent Balance")
                return
           
        elif option == 2:
            print("Please enter the number you want to purchase the airtime for")
            number = input("<< ")
            user_number = cls.number['user_number']
            if cls.number_check(number) and number != user_number:
                try:
                    amount = int(input("<< "))
                    
                except ValueError:
                    print("You were supposed to enter a number")  
                if cls.balance_check(amount, user_number):
                 
                    if number in cls.user_info:
                        if cls.pin_validation(user_number):
                            cls.user_info[user_number]["balance"] -= amount
                            print(f"You have purchased an airtime of GHS {amount} to {number}. Your new balance is {cls.user_info[user_number]["balance"]}")       
                        else:
                            print("Incorrect PIN")
                            return
                    else:
                        print("Number not found")
                        return
                else:
                    print("Insufficient Balance")
                    return
            else:
                print("Invalid Number or maybe you are trying to purchase the airtime for yourself")
                return      
    @classmethod
    def check_balance(cls):
        user_number = cls.number["user_number"]
        if cls.pin_validation(user_number):
            print(f"Your account balance is: {cls.user_info[user_number]["balance"]}")
        else:
            print("Incorrect PIN")
            return
    @classmethod
    def delete_account(cls):
        user_number = cls.number['user_number']
        if cls.pin_validation(user_number):
           del cls.user_info[user_number]  
           cls.save_users()
           cls.number = {}
        else:
            print("Invalid PIN")