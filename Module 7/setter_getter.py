class user:
    def __init__(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary

    #getter without any setter readonly attribute
    @property
    def age(self):
        return self._age

    #getter
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        return self.__salary+value
    

murad = user('koba',21,3100)
print(murad.age)
murad.salary = 4500
print(murad.salary)