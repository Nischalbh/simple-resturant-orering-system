from Menu_item import MenuItem
from resturant import Restaurant
from order import Order

momo = MenuItem("momo", 150)
coke = MenuItem("coke", 60)

r = Restaurant("Newari Khaja Ghar")
print(f"Resturant: {r.name}")
r.add_dish(momo)
r.add_dish(coke)

order = Order("Nischal")
print(f"{order.customer} ordered the following :")
order.add_item(r.menu[0])
order.add_item(r.menu[1])

print(f"Total is : Rs {order.total()}")
