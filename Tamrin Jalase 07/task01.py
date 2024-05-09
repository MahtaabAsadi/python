import random

userPoints = 0
computerPoints = 0

while True:
    user = input("Enter a choice (rock, paper, scissors): ")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    if user == computer:
        user = input("Enter a choice again (rock, paper, scissors): ")
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
    elif user == 'rock':
        if computer == 'paper':
           userPoints = userPoints + 1
           print('user won')
        else:
           computerPoints = computerPoints + 1
           print('computer won')
    elif user == 'paper':
        if computer == 'rock':
            userPoints = userPoints + 1
            print('user won')
        else:
           computerPoints = computerPoints + 1
           print('computer won')
    elif user == 'scissors':
        if computer == 'paper':
           userPoints = userPoints + 1
           print('user won')
        else:
           computerPoints = computerPoints + 1
           print('computer won')

    quitDecision = input('If you want to quit press "q": ')
    if quitDecision == 'q':
        break       

print('user points are: ')
print(userPoints)
print('computer points are: ')
print(computerPoints)
        