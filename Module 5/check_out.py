class shop:
    def __init__(self,name):
        self.name = name
        self.card = []
    
    def add_to_card(self,item,price,quantity):
        product = {'item':item,'price':price,'quantity':quantity}
        self.card.append(product)

    def remove(self,item):
        for items in self.card:
            print(items['item'])
            if items['item'] in items:
                print("yes")

    def check_out(self,ammount):
        total = 0
        for item in self.card:
            total += item['price'] * item['quantity']
        print('total price : ',total)
        if(ammount < total):
            print(f'Please give me {total-ammount} TK')
        else:
            sub = total - ammount
            print(f'Please take your money back :  {sub} TK')
            

        
murad = shop('Murad')
murad.add_to_card('alu',50,6)
murad.add_to_card('potol',10,3)
murad.remove('alu')
print(murad.card)
murad.check_out(200)