p1 = input("Player1 Enter your choice rock, paper, scissors > ")

# print the same print statement 20 times
print(" * * * NO CHEATING \n" * 20)

p2 = input("Player2 Enter your choice rock, paper, scissors > ")

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

