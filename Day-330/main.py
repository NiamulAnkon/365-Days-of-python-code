#birthday wish genarator

class birhtdaywish:
    def wish_birthday(self, someone, bdat, srchbdat):
        self.birthday_wish_message = f"Happy BirthDay to you {someone}"
        if bdat == srchbdat:
            print(self.birthday_wish_message)
        else:
            print("No one has birht day today :(")

if __name__ == "__main__":
    bdw = birhtdaywish()
    some = input("Whose birthday today: ")
    bdat = int(input("Birhtday date like this (1,2,333): "))
    srch = int(input("Search date: "))
    bdw.wish_birthday(some, bdat, srch)