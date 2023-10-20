class laptop:
    def __init__(self,brand,color,price,memory):
        self.brand = brand
        self.color = color
        self.price = price
        self.memory = memory

    def run(self):
        return f'Running laptop : {self.brand}'
    
    def coding(self):
        return f'larning python ar practiceing'

class Phone:
    def __init__(self,brand,color,price,dual_sim):
        self.brand = brand
        self.color = color
        self.price = price
        self.dual_sim = dual_sim


