class vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def move(self):
        pass

    def __repr__(self):
        return f'Name : {self.name},price : {self.price}'

class Bus(vehicle):
    def __init__(self,name,price,seat):
        self.seat = seat
        super().__init__(name,price)

bu = Bus('Lexas',1000,"A")
print(bu)