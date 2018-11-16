# ask age
# 18-21 wristband
# 21+ can drink normal entry
# otherwise too young sorry

age = input("Please enter age: > ")

# check non empty string
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("you will need a wristband")
    elif age >= 21:
        print("you can enter and have a drink")
    else:
        print("you are too young to enter")
else:
    print("please enter valid age")
    
