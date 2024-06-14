# random movie choser
#--------------------

# import area
import random


#the main body
class chose_movie:
    def chosed_movie(slef, usr_ctg):
        sci_fi = ["mv1", "mv2"]
        comedy = ["mv1", "mv2"]
        action = ["mv1", "mv2"]

        if usr_ctg == "sci-fi":
            chosen_movie_scifi = random.choice(sci_fi)
            print(chosen_movie_scifi)
        if usr_ctg == "comedy":
            chosen_movie_comedy = random.choice(comedy)
            print(chosen_movie_comedy)
        if usr_ctg == "action":
            chosen_movie_action = random.choice(action)
            print(chosen_movie_action)
        else:
            print("No catageory is saved")
    
if __name__ == "__main__":
    chs_mv = chose_movie()
    usr_ctg = input("Enter your catageory of movie: ")
    chs_mv.chosed_movie(usr_ctg)
