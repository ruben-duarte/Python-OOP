from item import Item
#inherit from Item
class Phone(Item):
      
      pay_rate = 0.55
      def __init__(self,name: str, price: float , quantity=0, broken_phones = 0):
        #call to super function to have access to all atributes and methods
        super().__init__(
            name, price, quantity
        )
        #Run validations to the received arguments
        assert broken_phones >= 0, f"broken phones {broken_phones} is not greater or equal to zero" 

        #assign to the self object

        self.broken_phones = broken_phones
