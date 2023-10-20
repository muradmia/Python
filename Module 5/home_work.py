class calculator:
    brand = "Casio"

    def add(self,num1,num2):
        return num1 + num2
    def deduct(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return num1 * num2
    def divide(self,num1,num2):
        return num1 / num2

cal = calculator()
print("add method is :",cal.add(10,20))
print("Subtract method is :",cal.deduct(20,30))
print("divide method is :",cal.divide(25,30))
print("Multipy method is :",cal.multiply(10,2))