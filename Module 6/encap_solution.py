#encapsulation --> hide details
# access modifier ,public,protected,private

class Bank:
    def __init__(self,holder_name,deposit,branch):
        self.holder_name = holder_name #it is a public variable
        self._branch = branch #it is a protected variable
        self.__balance = deposit #It is a private variable

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokir not allow' 


    def get_balance(self):
        return self.__balance #get the private value
    
murad = Bank('Murad',10000,'Panchdona')
""" print(murad.holder_name)
murad.deposit(100)
print(murad.get_balance())
print(murad._branch) """
print(murad._Bank__balance)