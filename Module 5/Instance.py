""" class shop:
    cart = []
    def __init__(self,name):
        self.name = name
    
    def add_card(self,item):
        self.cart.append(item)
    
murad = shop("Nike")
murad.add_card("Shoes")
murad.add_card("Catch")
print(murad.cart)

 """

class shop:
    shopping_mall = 'jamuna'
    def __init__(self,name):
        self.name = name
        self.cart = [] #card is instance attribute
    
    def add_card(self,item):
        self.cart.append(item)
    
murad = shop("Nike")
murad.add_card("Shoes")
murad.add_card("Catch")
print(murad.cart)


tanvir = shop("Easy")
tanvir.add_card("shirt")
tanvir.add_card("t-shirt")
print(tanvir.cart)