class family:
    def __init__(self,name):
        self.name = namme
    
class school():
    def __init__(self,id,level):
      self.id = id
      self.level = level


class sport():
    def __init__(self,game):
        self.game = game
        

class student(family,school,sport):
    def __init__(self,address):
        self.address = address
        sport.__init__(self,game)
        school.__init__(self,id,level)
        family.__init__(self,name)
    
    def __repr__(self) -> str:
        return f'ad : {self.address}, : {self.id}, : {self.level}, {self.game}'

s = student('Dhaka',12,32,'PUBG')
print(s)