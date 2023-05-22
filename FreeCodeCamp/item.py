import csv
class Item:
   pay_rate = 0.8 #20% discount rate // class attribute
   all = []

   def __init__(self,name: str, price: float , quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"price {price} is negative"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero" 

        #assign to the self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

   @property
   #property decorator  = read only atributte
   def name(self):
       return self.__name

   def total_price(self):
        return self.price*self.quantity
   

   def apply_discount(self):
       self.price = self.price * self.pay_rate
  
   @classmethod
   def instantiate_from_csv(cls):
       with open('G:\Python\PY-OOP\FreeCodeCamp\items.csv', 'r') as f:
           reader = csv.DictReader(f)
           items = list(reader)
       for item in items:
           Item(
               name = item.get('name'),
               price = float(item.get('price')),
               quantity = int(item.get('quantity')), 
           )
   

   @staticmethod
   def is_integer(num):
       # count the number of  floats
       if isinstance(num, float):
           #count the floats that are point zero
           return num.is_integer()
       elif isinstance(num,int):
           return True
       else:
           return False
       

   def __repr__(self):
       return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
   
