import pyautogui
class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_wirhdraw = 100
        self.max_wirhdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if(ammount > 0):
            self.balance+amount
        else:
            print("zero ammount")
    
    def withdraw(self,amount):
        if amount < self.min_wirhdraw:
            print(f'fokira you cannot withdraw : {self.min_wirhdraw}') 
        elif amount > self.max_wirhdraw:
            print(f'bank fokir hoye jabe : {self.max_wirhdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}') 
            print(f'your balance after withdraw : {self.balance}')

from time import sleep
sleep(3)
pyautogui.write("--------well come to bank-------",interval=0.25)   
brac = bank(10000)
print(brac.withdraw(225))
