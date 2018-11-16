# from numbers 1 to 20 both inclusive print odd or even and unlucky for 9 and 13

print("using for loop:")
for num in range(1, 21):
    if num == 9 or num == 13:
        print("{} - UNLUCKY" .format(num))
    elif (num % 2) == 0:
        print("{} - even" .format(num))
    else:
        print("{} - odd" .format(num))

print("using while loop")        
num = 1
while num < 21:
    if num == 9 or num == 13:
        print("{} - UNLUCKY" .format(num))
    elif (num % 2) == 0:
        print("{} - even" .format(num))
    else:
        print("{} - odd" .format(num))
    num += 1

# print emoji smily faces 10 times

for x in range(1, 11):
    print("\U0001f600 " * x)

x = 1
while x < 11:
    print("\U0001f600 " * x)
    x += 1
    
# without using the multiplier in print

for num in range(1, 11):
    count = 1
    smiley = ""
    while count <= num:
        smiley += " \U0001f600"
        count += 1
    print(smiley)