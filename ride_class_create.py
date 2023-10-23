from abc import ABC, abstractmethod
class user(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.id = 0
        self.__nid = nid
        self.email = email
        self.money = 0

    @abstractmethod
    def display_profie(self):
        raise NotImplementedError
    
class rider(user):
    def __init__(self, name, email, nid,curent_location) -> None:
        self.curent_ride = None
        self.money = 0
        self.curent_location = curent_location
        super().__init__(name, email, nid)

    def display_profie(self):
        print(f'name : {self.name},email {self.email}')

    def load_cash(self,ammount):
        if ammount > 0:
            self.money += ammount
    
    def update_location(self,curent_location):
        self.curent_location = curent_location


    def ride_request(self,location,dectination):
        if not self.curent_ride:
            #onk kaj ache eii khane
            ride_request = 0
            self.curent_ride = None
class driver(user):
    def __init__(self, name, email, nid,curent_location) -> None:
        super().__init__(name, email, nid)
        self.curent_locatoin = curent_location

    def display_profie(self):
        print(f'name : {self.name} email : {self.email}')

    def accept_ride(self,ride):
        ride.set_rider(self)


class ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location



    
