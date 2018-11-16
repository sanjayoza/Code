from random import choice, randint

#question 1
x = randint(-100, 100)
while x == 0:     # make sure x isnt 0
    x = randint(-100, 100)

y = randint(-100, 100)
while y == 0:     # make sure y isnt 0
    y = randint(-100, 100)
print(x)
print(y)

if x > 0 and y > 0:
    print("both positive numbers")
elif x > 0 and y < 0:
    print("x is positive y is negative")
elif x < 0 and y > 0:
    print("x is negative y is positive")
else:
    print("both are negative")
    
#question 2 - set to true if call in sick if you are sick and have sick days,
#             you are kinda sick and hate your job and sick days remaining

#randomly assign values to these variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = None   # set to True or False
calling_in_sick = False

if actually_sick == True and sick_days < 10:
    calling_in_sick = True
elif kinda_sick == True and hate_your_job == True and sick_days < 10:
    calling_in_sick = True
else:
    calling_in_sick = False
    
print("calling_in_sick {}" .format(calling_in_sick))
