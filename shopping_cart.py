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

    def print_item_list(self):
        receipt = ""
        for item in self.item_list:
            receipt += f"{item.name}".ljust(26, " ") + f"EUR  {item.price:.2f}\n"
        return receipt.replace(".", ",").strip()
    
    def print_receipt(self):
        receipt = self.print_item_list()
        receipt += f"\n\nTOTAL                     EUR  {self.total_price():.2f}"
        return receipt.replace(".", ",")

    def get_item_count(self, item_name:str):
        pass

class UnderflowError(Exception):
    pass

