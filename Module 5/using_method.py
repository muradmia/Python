class phone:
    price = 15000
    brane = "Vivo"
    color = "Blue"
    feature = ["camera","speaker","hammer"]


    def call(self):
        print("calling method")

    def send_sms(self,phone,sms):
        text = f'sending sms to {phone} ans message : {sms}'
        return text

my_phone = phone()
print(my_phone.feature)
result = my_phone.send_sms(12312212,'gdss')
print(my_phone.call())
print(result)