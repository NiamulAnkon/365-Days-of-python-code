class Solution:
    def __init__(self):
        self.height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.bricks = 5
        self.ladders = 5
        self.jumps = 2
        self.floor = []
        self.opts = {"bricks": self.bricks, "ladders": self.ladders, "jumps": self.jumps}

    def main_menu(self):
        print("Buildings Heights:\n{}".format(self.height))
        usr_choice = int(input("Enter on which building you want to go (1-14): "))
        if usr_choice in range(1, 15):
            opt_choice = input("Enter how you want to go there (bricks/ladders/jumps): ")
            if opt_choice in self.opts and self.opts[opt_choice] > 0:
                self.opts[opt_choice] -= 1 
                self.floor.append(usr_choice)  
                print('Congratulations! You reached floor {}\nNow you have {} {} left.'.format(usr_choice, self.opts[opt_choice], opt_choice))
            else:
                print("Invalid option or no more remaining!")

if __name__ == "__main__":
    solution = Solution()
    solution.main_menu()
