def double():
    print('first')
    def inn():
        print('second')
    return inn

#print(double()())

def to_do(work):
    print('start work')
    work()
    print('end work')

def coding():
    print('start coding')

to_do(coding)
#print(to_do())