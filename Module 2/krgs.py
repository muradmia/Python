""" def name(first ,last):
    return f'{first}{last}'
result = name(last = 'Murad',first = 'Mia')
print(result)

def multiple(num,num1):
    sum = num+num1
    multi = num*num1
    dev = num/num1
    return sum, multi,dev

num2 = input()
num2_int = int(num2)
num3 = input()
num3_int = int(num3)
everytging = multiple(num2_int,num3_int)
print(everytging)
 """
def mul(f,l,**adi):
    sett = f'{f}{l}'
    for key,vale in adi.items():
        print(key,vale)
    return sett

res = mul(f = 'murad',l = 'mia',title = "muradaa")
print(res)