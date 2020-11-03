#Rock-Paper-Scissors

#Stage 1/5: Unfair computer

user_choise = str(input())

def unfair(user_choise):
    if user_choise == 'scissors':
        comp_option = "rock"
        print(f"Sorry, but the computer chose {comp_option}")
    elif user_choise == 'rock':
        comp_option = "paper"
        print(f"Sorry, but the computer chose {comp_option}")
    elif user_choise == 'paper':
        comp_option = "scissors"
        print(f"Sorry, but the computer chose {comp_option}")
    
unfair(user_choise)

#2/5: Equalizing chances
# Read user's input specifying the option that user has chosen
# Choose a random option
# Compare the options and determine the winner
# Output a line depending on the result of the game:
# Lose -> Sorry, but the computer chose <option>
# Draw -> There is a draw (<option>)
# Win -> Well done. The computer chose <option> and failed

import random

game_vars = 'scissors', 'rock', 'paper'

win_game_map = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors'
}

computer_option = random.choice(game_vars)

user_choise = str(input())

if user_choise == computer_option:
    print(f'There is a draw ({user_choise})')
elif win_game_map[user_choise] == computer_option:
    print(f'Sorry, but the computer chose {computer_option}')
else:
    print(f'Well done. The computer chose {computer_option} and failed')

#Stage 3/5: Endless game
# Take an input from the user
# If the input is !exit, output Bye! and stop the game
# If the input is the name of the option, then:
# Pick a random option
# Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
# Lose -> Sorry, but the computer chose <option>
# Draw -> There is a draw (<option>)
# Win -> Well done. The computer chose <option> and failed
# If the input corresponds to anything else, output Invalid input
# Do it all over again

import random

game_vars = 'scissors', 'rock', 'paper'

win_game_map = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors'
}

while True:
    user_choise = str(input())
    computer_option = random.choice(game_vars)
            
    if user_choise == '!exit':
        print("Bye!")
        break
    
    elif user_choise not in game_vars and user_choise != '!exit':
        print("Invalid input")
    elif user_choise == computer_option:
        print(f'There is a draw ({user_choise})')
    elif win_game_map[user_choise] == computer_option:
        print(f'Sorry, but the computer chose {computer_option}')
    else:
        print(f'Well done. The computer chose {computer_option} and failed')


#4/5: Scoring the game
# Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
# Read input specifying the user's name and output a new line Hello, <name>
# Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
# Play the game by the rules defined on the previous stages:
# Read user's input
# If the input is !exit, output Bye! and stop the game
# If the input is the name of the option, then:
# Pick a random option
# Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
# Lose -> Sorry, but the computer chose <option>
# Draw -> There is a draw (<option>)
# Win -> Well done. The computer chose <option> and failed
# For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
# If the input corresponds to anything else, output Invalid input
# Play the game again

import random

game_vars = 'scissors', 'rock', 'paper'

win_game_map = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors'
}

user_name = str(input('Enter your name: '))
print(f"Hello, {user_name}")

user_score = 0

#read file rating.txt and check if there's a record for the user with the same name
rating = open("rating.txt", 'r')
rating_list = rating.readlines()

for lines in rating_list:
    if user_name in rating_list:
        # index_user = rating_list.index(user_name)
        # user_score = int(rating_list[index_user + 1])
        temp = line.split()
        user_score = int(temp[1])


# def game_score(user_score, state_game):    
#     if draw:
#         user_score += 50
#     elif win:
#         user_score += 100
#     return user_score


while True:
    # global user_name, user_score
   
    user_choise = str(input())
    
            
    if user_choise == '!exit':
        print("Bye!")
        break
    
    if user_choise == '!rating':
        print(f'Your rating: {user_score}')
        continue

    if user_choise not in game_vars and user_choise != '!exit':
        print("Invalid input")
        continue
    
    computer_option = random.choice(game_vars)

    if user_choise == computer_option:
        user_score += 50
        print(f'There is a draw ({user_choise})')
        

    elif win_game_map[user_choise] == computer_option:
        print(f'Sorry, but the computer chose {computer_option}')
    else:
        user_score += 100
        print(f'Well done. The computer chose {computer_option} and failed')


# 5/5: More options
# Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
# Read input specifying the user's name and output a new line Hello, <name>
# Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
# Read input specifying the list of options that will be used for playing the game (options are separated by comma). If the input is an empty line, play with default options.
# Output a line Okay, let's start
# Play the game by the rules defined on the previous stages:
# Read user's input
# If the input is !exit, output Bye! and stop the game
# If the input is the name of the option, then:
# Pick a random option
# Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
# Lose -> Sorry, but the computer chose <option>
# Draw -> There is a draw (<option>)
# Win -> Well done. The computer chose <option> and failed
# For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
# If the input corresponds to anything else, output Invalid input
# Play the game again (with the same options that were defined before the start of the game)

import random
# "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire"
cycle = ['rock','paper','scissors']
name = input("Enter your name: ")
print("Hello, " + name)
score = 0
f = open("rating.txt", 'r')
for line in f:
    if name in line:
        temp = line.split()
        score = int(temp[1])

options = input()
if options:
    cycle = options.split(",")
length = len(cycle)
print("Okay, let's start")

while True:

    player_choice = input()

    if player_choice == "!exit":
        print("Bye!")
        break

    if player_choice == "!rating":
        print(f"Your rating: {score}")
        continue

    if player_choice not in cycle:
        print("Invalid input")
        continue

    computers_choice = random.choice(cycle)

    if player_choice == computers_choice:
        score += 50
        print("There is a draw (" + computers_choice + ")")
        continue
    
    win = True
    for i in range(length // 2):
        if (cycle.index(player_choice) + i + 1) % length == cycle.index(computers_choice):
            win = False
            break

    if win == True:
        score += 100
        print("Well done. The computer chose " + computers_choice + " and failed")
        continue

    if win == False:
        print("Sorry, but the computer chose " + computers_choice)


























