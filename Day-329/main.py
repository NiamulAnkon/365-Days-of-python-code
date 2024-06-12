#import area
import random
import time
#-------------#
#classes
class pic_games:
    #function for chosing random game
    def chose_random_games_to_play(slef, gamelist, usrcmd):
        while True: #using while loop to loop through everything
            if usrcmd == "y":
                slef.chosen_game = random.choice(gamelist)
                print(f"The game that is chosen is: {slef.chosen_game}")
                time.sleep(4.9)
                usr_chs = input("Wanna do again y/n: ")
                if usr_chs == "n":
                    break
                else:
                    continue
            else:
                print("thankyou")
                break

if __name__ == "__main__":
    pg = pic_games()
    game_lists = ["Kabaddi", "thief and police", "Ghost of Thushima", "Valorant", "Pubg", "Catch catch", "Football", "Cricket"]
    usr_cmd = input("Do you want to chose the a game to play y/n: ")
    pg.chose_random_games_to_play(game_lists, usr_cmd)