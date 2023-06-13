from item import Item
from phone import Phone
from keyboard import Keyboard

Item.instantiate_from_csv()

item1= Item("New Item",800,6)
item1.apply_increment(0.2)
item1.apply_discount()
print(item1) 

item2 = Phone('Samsung', 1000,3)
item2.apply_increment(0.2)
print(item2.price)

item3 = Keyboard('Sony', 1000,3)
item3.apply_increment(0.2)
print(item3.price)






