class Item:
   pay_rate = 0.8 #20% discount rate // class attribute
   all = []

   def __init__(self,name: str, price: float , quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"price {price} is negative"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero" 

        #assign to the self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)


   def total_price(self):
        return self.price*self.quantity
   

   def apply_discount(self):
       self.price = self.price * self.pay_rate


   def __repr__(self):
       return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone",100, 1)
item2 = Item("Laptop",1000, 3)
item3 = Item("Cable",10, 5)
item4 = Item("Mouse",50, 5)
item5 = Item("Keyboard",75, 5)

print(Item.all)
for instance in Item.all:
    print(instance.name)