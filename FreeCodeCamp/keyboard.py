from item import Item
#inherit from Item
class Keyboard(Item):
      
      pay_rate = 0.7
      def __init__(self,name: str, price: float , quantity=0):
        #call to super function to have access to all atributes and methods
        super().__init__(
            name, price, quantity
        )
