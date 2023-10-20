age = input()
age_int = int(age)

if(age_int > 5):
    print(age)
elif (age_int == 5) :
    print("wrong")
else :
    print("hey")


boss = False
if age_int > 1 :
    print("wrong")
    if boss == True :
        print("hey")
    else:
        print("hello")
elif age_int == 2:
    print("right")