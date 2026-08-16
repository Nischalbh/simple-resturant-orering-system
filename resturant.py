class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_dish(self, item):
        self.menu.append(item)

    def show_menu(self):
        for item in self.menu:
            print(f"{item.name} - Rs {item.price}")
