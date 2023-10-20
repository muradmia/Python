class Student:
    def __init__(self,name,curent_class,id):
        self.name = name
        self.curent_class = curent_class
        self.id = id

    def __repr__(self) -> str:
        return f'Name : {self.name}, Class : {self.curent_class}, ID : {self.id}'

class Teachers:
    def __init__(self,name,sub,id):
        self.name = name
        self.sub = sub
        self.id = id

    def __repr__(self) -> str:
        return f'Name : {self.name}, Sub : {self.sub}, id : {self.id}'

class school:
    def __init__(self,name):
        self.name = name
        self.teacher = []
        self.students = []
    
    def add_teacher(self,name,sub):
        id = len(self.teacher)+1
        teachers = Teachers(name,sub,id)
        self.teacher.append(teachers)
        return f'name : {self.name},id : {id}'

    def enroll(self,name,ammount):
        if ammount < 6500:
            return f'not enough fee'
        else:
            id = len(self.students)
            student = Student(name,'C',id)
            self.students.append(student)
            return f'name : {self.name} Id is : {id}'
        
    def __repr__(self) -> str:
        print('our school ',self.name)
        print('Our teachers')
        for it in self.teacher:
            print(it)
        
        print('Our student')
        for i in self.students:
            print(i)
        
        return f'all done'

phitron = school("Phitron")
phitron.enroll('Murad',6500)
phitron.enroll('Sadia',6500)
phitron.add_teacher('Sadik','DSA')
print(phitron)
