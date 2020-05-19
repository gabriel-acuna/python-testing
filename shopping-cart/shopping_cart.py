class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def code(self):
        return f'{self.name}-1234567890'
    

class NotExistsItemError(Exception):
    pass

class ShoppingCart:

    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def contains_item(self):
        return len(self.items) > 0
    
    def remove_item(self, item):
        for i in self.items:
            if i['item'] == item: self.items.remove(i)

    def total(self):
        return sum([ item['item'].price * item['quantity'] for item  in self.items])

    def get_item(self, item):
       for i in self.items:
           if i['item'] == item: return self.items[self.items.index(i) -1]['item']
           else: raise NotExistsItemError("Item doesn't exist!")

    def clear_cart(self):
        self.items.clear()
