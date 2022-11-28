class ShoppingCart:
    
    def __init__(self):
        self.item_list = []

    @property
    def item_count(self):
        return len(self.item_list)


    def add(self, item):
        self.item_list.append(item)
        
    def remove(self, item):
        if self.item_count == 0:
           raise UnderflowError 
        self.item_list.remove(item)

    def items(self):
        return self.item_list

    def total_price(self):
        total_price = 0
        for item in self.item_list:
            total_price += item.price
            
        return total_price

class UnderflowError(Exception):
    pass

