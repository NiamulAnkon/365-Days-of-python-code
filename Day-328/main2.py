import random
def chose_games(gamelist, gmsamnt):
    i = 0
    if i <= gmsamnt:
        chosen_game = random.choice(gamelist)
        i += 1
        print(chose_games)
    else:
        print("Something Went wrong")

if __name__ == "__main__":
    game_list = ["Football", "cricket", "Kabaddi"]
    games_amount = 2
    chose_games(game_list, games_amount)
