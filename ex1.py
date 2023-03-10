import random

#1 Welcome User

print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

#2 Ask user how many rounds they want to play

rounds = int(input("How many rounds would you like to play? ==> "))

#3 Make a list of the 5 choices

Choices = ["Rock","Paper","Scissors","Lizard","Spock"]

# User defined function

def beats(x,y):
    if (x in ["1", "Rock"] and y in["Scissors","Lizard"] or 
        x in ["2", "Paper"] and y in ["Rock","Spock"] or 
        x in ["3", "Scissors"] and y in ["Paper","Lizard"] or 
        x in ["4", "Lizard"] and y in ["Paper","Spock"] or 
        x in ["5", "Spock"] and y in ["Rock","Scissors"]):
        return True
    elif x == y:
        return None
    else:
        return False
    
def percentage(i, n):
    percent = (i / n) * 100
    return round(percent , 1)

    
#4 Make accumulator variables for player and bot wins

player_wins = 0
bot_wins = 0
draws = 0

#5 Make accumulators for player choices

player_rock = 0
player_paper = 0
player_scissors = 0
player_lizard = 0
player_spock = 0

#6 Make accumulators for bot choices

bot_rock = 0
bot_paper = 0
bot_scissors = 0
bot_lizard = 0
bot_spock = 0

#5 Make a for loop for amount of rounds

for num in range(rounds):

    #6 Display round

    print("Round", num + 1, "of", rounds,":")

    #7 Ask user about their choice

    player_choice = input(

'''
What item do you choose?
1 - Rock
2 - Paper
3 - Scissors
4 - Lizard
5 - Spock

Answer by entering the corresponding name or number.

Your Answer ==> '''

)
    #8 randomly choose bot choice

    bot_choice=random.choice(Choices)
    print(f"I chose: {bot_choice}\n")

    #9 Tally the player choice

    if player_choice in ["1", "Rock"]:
        player_rock += 1
    elif player_choice in ["2", "Paper"]:
        player_paper += 1
    elif player_choice in ["3", "Scissors"]:
        player_scissors += 1
    elif player_choice in ["4", "Lizard"]:
        player_lizard += 1
    elif player_choice in ["5", "Spock"]:
        player_spock += 1

    #10 Tally the bot choices
    if bot_choice == "Rock":
        bot_rock += 1
    elif bot_choice == "Paper":
        bot_paper += 1
    elif bot_choice == "Scissors":
        bot_scissors += 1
    elif bot_choice == "Lizard":
        bot_lizard += 1
    elif bot_choice == "Spock":
        bot_spock += 1

    #9 Determine winner using function

    if beats(player_choice,bot_choice) == True:
        print("You win this round! \n")
        player_wins += 1

    elif beats(player_choice,bot_choice) == False:
        print("I win this round! \n")
        bot_wins += 1

    elif beats(player_choice,bot_choice) == None:
        print("This round was a tie! \n")
        draws += 1

# Determine the winner of the entire match

if player_wins > bot_wins:
    winner = f"Player wins the match with the score of {player_wins} - {bot_wins} !"
elif player_wins < bot_wins:
    winner = f"The Bot wins the match with the score of {bot_wins} - {player_wins} !"
else:
    winner = f"The winners are tied at {player_wins} - {bot_wins} !"

# Print Match Summary

print('Good Game! Here are the statistics for the match!')

print(f'''
Your statistics for this match:

Player choices summary:


Rock -- {player_rock} rounds out of {rounds} rounds or {percentage(player_rock, rounds)}% of the time!
Paper -- {player_paper} rounds out of {rounds} rounds or {percentage(player_paper, rounds)}% of the time!
Scissors -- {player_scissors} rounds out of {rounds} rounds or {percentage(player_scissors, rounds)}% of the time!
Lizard -- {player_lizard} rounds out of {rounds} rounds or {percentage(player_lizard, rounds)}% of the time!
Spock -- {player_spock} rounds out of {rounds} rounds or {percentage(player_spock, rounds)}% of the time!

Bot choices summary:

Rock -- {bot_rock} rounds out of {rounds} rounds or {percentage(bot_rock, rounds)}% of the time!
Paper -- {bot_paper} rounds out of {rounds} or rounds {percentage(bot_paper, rounds)}% of the time!
Scissors -- {bot_scissors} rounds out of {rounds} or rounds {percentage(bot_scissors, rounds)}% of the time!
Lizard -- {bot_lizard} out of rounds {rounds} or rounds {percentage(bot_lizard, rounds)}% of the time!
Spock -- {bot_spock} out of rounds {rounds} or rounds {percentage(bot_spock, rounds)}% of the time!

You won {player_wins} rounds out of {rounds} rounds!
The bot has won {bot_wins} rounds out of {rounds} rounds!
There were {draws} draws out of {rounds} rounds!

{winner}

''')

