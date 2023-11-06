import random

words = ["python", "java", "c", "csharp","javascript", "cplusplus", "ruby"]
word = random.choice(words)


total_chances = 12
print(f"Weocome to HangMan \nYou have only {total_chances} Chances")
guessed_word = "-" * len(word)

while total_chances != 0:

    print(guessed_word)

    letter = input("Guess the letter: ").lower()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
                print(guessed_word)
        if guessed_word == word:
            print("Comngrats You have won!!!!!")
            break
    else:
        total_chances -= 1
        print("Incorrect answer")
        print(f"Total chances you have are: {total_chances}")
else:   
    print(f"Game Over \nYou Lose \nAll the chances ar exhausted \nThe correct word is {word}")