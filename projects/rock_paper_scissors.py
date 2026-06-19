import random

choices = ["rock", "paper", "scissor"]

#User choice
user = input("Enter your choice rock, paper or scissors: ")

#Computer choice
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

#Both choose the same
if user == computer:
    print("It's a Tie!")

#User winning conditions
elif (user == "rock" and computer == "scissor") or (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper"):
    print("You Win!")

#User lost
else:
    print("You Lost, Try again!")
