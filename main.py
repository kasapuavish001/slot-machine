#to create a global 

def deposit():
    while True:
        amount = input("Enter amount you like to deposit bro? $")
        if amount.isdigit():
            amount = int(amount)
            if(amount > 0):
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Please Enter a Number bro.")

    return amount

def main():
    balance = deposit()

