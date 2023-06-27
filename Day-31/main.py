#BETING GAME
import random

def betting_game():
    print("Welcome to the betting game!")
    team1 = input("Enter the name of Team 1: ")
    team2 = input("Enter the name of Team 2: ")
    bet_amount = int(input("Enter the amount you want to bet: "))
    user_choice = input(f"Which team do you want to bet on - {team1} or {team2}? ")
    
    if user_choice.lower() == team1.lower():
        print(f"You have bet {bet_amount} on {team1}.")
    elif user_choice.lower() == team2.lower():
        print(f"You have bet {bet_amount} coins on {team2}.")
    else:
        print(f"Chose between {team1} or {team2}")
        return
    
    winning_team = random.choice([team1, team2])
    print(f"The winning team is {winning_team}!")
    
    if winning_team.lower() == user_choice.lower():
        print(f"Congratulations! You have won {bet_amount * 2}!")
    else:
        print("Sorry, you lost the bet you don't have enough knowledge.😂")
    
betting_game()