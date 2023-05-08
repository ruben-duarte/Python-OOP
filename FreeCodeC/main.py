class Item:
   pay_rate = 0.8 #20% discount rate

   def __init__(self,name: str, price: float , quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"price {price} is negative"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero" 


        #assign to the self object
        self.name = name
        self.price = price
        self.quantity = quantity


   def total_price(self):
        return self.price*self.quantity


item_1 = Item('bike', 45)    
item_2 = Item('phone', 350, 2)
item_2.has_ear_buds = False

print(item_1.name)
print(item_2.name)
print(item_1.price)
print(item_2.price)
print(item_1.quantity)
print(item_2.quantity)
print(item_1.total_price())
print(Item.__dict__)