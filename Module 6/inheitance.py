
class gadget:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f'Running laptop : {self.brand}'

class laptop:
    def __init__(self,memory):
        
        self.memory = memory

    def run(self):
        return f'Running laptop : {self.brand}'
    
    def coding(self):
        return f'larning python ar practiceing'

class Phone(gadget):
    def __init__(self,brand,price,color,dual_sim):
        self.dual_sim = dual_sim
        #super(gadget).__init__(brand,price,color)
        super().__init__(brand,price,color)

    def run(self):
        return f'Running laptop : {self.brand}'
    
    def coding(self):
        return f'larning python ar practiceing'

    def __repr__(self) -> str:
        return f'Phone : {self.brand},color : {self.color} ,price : {self.price}, sim : {self.dual_sim}'

#ph = Phone('xiomi',15000,'blue',True)
ph = Phone('xiomi',1522,'Black',True)
print(ph)

