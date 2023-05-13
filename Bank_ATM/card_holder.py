class Card_holder:

    def __init__(self, cardNum, pin , firstname, lastname, balance):
        self.cardNum = cardNum
        self.cardPin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
    

    #Getter
    def get_cardNum(self):
        return self.cardNum
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_balance(self):
        return self.balance
    
    def get_pin(self):
        return self.cardPin
    
    #setter
    def set_cardNum(self, new_value):
        self.cardNum = new_value

    def set_firstname(self, new_value):
        self.firstname = new_value

    def set_lastname(self, new_value):
        self.lastname = new_value

    def set_balance(self, new_value):
        self.balance = new_value
    
    def set_pin(self, new_value):
        self.pin = new_value

    def print_out(self):
        print("card: " + self.cardNum)    
        print("pin: " + self.pin)
        print("firstname: " + self.firstname)
        print("lastname: " + self.lastname)
        print("balance: " + self.balance)

        