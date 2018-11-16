# using computer as a player
import random
# change the input to lower
p1 = input("Player Enter your choice rock, paper, scissors > ").lower()

rand_num = random.randint(0, 2)
if rand_num == 0:
    p2 = "rock"
elif rand_num == 1:
    p2 = "paper"
else:
    p2 = "scissors"
print("player2 choice " + p2)
if p1 == p2:
    print("It is a tie")
elif p1 == "rock":
    if p2 == "scissors":
        print("player 1 wins")
    if p2 == "paper":
        print("player 2 wins")
elif p1 == "paper":
    if p2 == "scissors":
        print("player2 wins")
    if p2 == "rock":
        print("player1 wins")
elif p1 == "scissors":
    if p2 == "paper":
        print("player1 wins")
    if p2 == "rock":
        print("player2 wins")
else:
    print("something went wrong")
