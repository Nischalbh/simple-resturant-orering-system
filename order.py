class Order:
    def __init__(self, customer):
        self.customer = customer
        self.item = []

    def add_item(self, item):
        self.item.append(item)
        print(f"Added {item.name}")

    def total(self):
        return sum(item.price for item in self.item)
