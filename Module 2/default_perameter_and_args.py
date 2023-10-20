def sum(num,num1,num3=0):
    return num+num1

total = sum(12,2)
print(total)

def all_sum(num1,num2,*numbers):
    s = 0
    print(numbers)
    for i in numbers:
        s +=i
        print(s)

all_sum(12,312,31,41,31)

for i in range(1,10):
    print(i)