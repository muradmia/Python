class company:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.bus = []
        self.router = []
        self.driver = []
        self.counters = []
        self.manager = []
        self.supervisor = []


class driver:
    def __init__(self,name,lisence,age):
        self.name = name
        self.lisence = lisence
        self.age = age

class counter:
    def __init__(self,address,route):
        pass
    def purchase_ticker(self,start,destination):
        pass
class passenger:
    def __init__(self,address,name):
        pass

class supervisor:
    def __init__(self,name):
        pass