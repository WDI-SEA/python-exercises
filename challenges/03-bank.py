# print("Welcome to Chase bank.")
# print("Have a nice day!")

def bank_activity():
    init_balance= int(5000)
    print(f"Your current balance is \n{init_balance}")
    active=True
    while active == True:
        text = input("What would you like to do today? (deposit, withdraw, check_balance) ")
        if text == "deposit":
            text=input("How much would you like to deposit?\n")
            init_balance = init_balance + int(text)
            print(f"Your current balance is \n{init_balance}")
            text=input("Are you done? yes/no ")
            if text == "yes":
                    active = False
                    print("Have a nice day!")
            elif text == "no":
                    active == True
        if text == "withdraw":
            text=input("How much would you like to withdraw?\n")
            init_balance = init_balance - int(text)
            print(f"Your current balance is \n{init_balance}")
            text=input("Are you done? yes/no ")
            if text == "yes":
                    active = False
                    print("Have a nice day!")
            elif text == "no":
                    active == True
        if text == "check_balance":
            print(f"Your current balance is \n{init_balance}")
            text=input("Are you done? yes/no ")
            if text == "yes":
                    active = False
                    print("Have a nice day!")
            elif text == "no":
                    active == True
bank_activity()