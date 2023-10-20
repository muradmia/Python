class Phone:
    manufactured = 'Bangladesh'


    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,num,sms):
        text = f'Sending sms to : {num} sms is : {sms}'
        return text
    
my_phone = Phone('Murad','Vivo',30000)
print(my_phone.manufactured,my_phone.brand,my_phone.price)
print(my_phone.send_sms(54424,"Hi"))