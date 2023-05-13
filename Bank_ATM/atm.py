from card_holder import Card_holder

def print_menu():
    #print  options for the menu
    print("="*80)
    print("Please select one of the following options")
    print("""
    Welcome to ATM

    1. Deposit
    2. Withdraw
    3. Show balance
    4. Exit

    """)

def deposit(Card_holder):
    try:
        deposit = float(input("How much to deposit?:  "))
        Card_holder.set_balance(Card_holder.get_balance()+ deposit)
        print(f"Thank you for your deposit. Your new balance is ${Card_holder.get_balance()}")
    except:
        print("Invalid input")

def withdraw(Card_holder):
    try:
        withdraw = float(input("How many do you want to withdraw:   "))
        #check if user has enough money
        if Card_holder.get_balance() < withdraw:
            print("Insufficient funds")
        else:
            Card_holder.set_balance(Card_holder.get_balance() - withdraw)
            print("Your balance is enough to withdraw")
    except:
        print("Invalid input")

def check_balance(Card_holder):
    print("Your balance is:  ", Card_holder.get_balance())


if __name__ == "__main__":
    current_user = Card_holder("","","","","")

    list_of_card_holders = []
    list_of_card_holders.append(Card_holder("343434556", 2354, "james", "Jones",  200))
    list_of_card_holders.append(Card_holder("543433556", 7364, "Frida", "Jones",  200))
    list_of_card_holders.append(Card_holder("743434556", 8354, "Jackie", "James",  200))
    list_of_card_holders.append(Card_holder("943434556", 9354, "Albert", "Jones",  200))
    list_of_card_holders.append(Card_holder("243434556", 2754, "John", "Smith",  200))
   
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please enter your debit card number: ")
            #check  
            debit_match = [holder for holder in list_of_card_holders if holder.cardNum == debitCardNum]
            if len(debit_match)>0:
                current_user = debit_match[0]
                break
            else:
                print("Card number is not recognized. Please try again")
        except:
            print("Card number is not valid")

    #prompt for pin
    while True:
            try:
                userPin = int(input("Please enter your PIN: ").strip())
                if current_user.get_pin() == userPin:
                    break
                else:
                    print("Pin number is not valid")
            except:
                print("Pin number is not valid")

    ##Print options
    print("+"*40)
    print("Welcome ",current_user.get_firstname(), "🎉  ")
    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input, please try again")
        
        if option== 1:
            deposit(current_user)
        elif option== 2:
            withdraw(current_user)
        elif option== 3:
            check_balance(current_user)
        elif option== 4:
            break
        else:
            option = 0

    print("Thank you have a nice day")