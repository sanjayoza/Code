import random

keep_playing = "y"

user_input = 0
while True:
    ran_num = random.randint(1, 10)
    user_input = input("Enter your guess 1 to 10 > ")
    user_input = int(user_input)
    print("user_input " .format(user_input))
    if user_input == ran_num:
        print("you win")
        keep_playing = input("Keep playing (y/n) > ")
        if keep_playing == "n":
            print("Thank you for playing - bye")
            break

    elif user_input < ran_num:
        print("too low {}" .format(ran_num))
    else:
        print("too high {}" .format(ran_num))
