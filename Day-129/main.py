from itertools import product
import string

min_len = int(input("Enter minimum length of the password: "))
max_len = int(input("Enter the maximum length of the password: "))
counter = 0
char = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open("wordlist.txt", "w")
for i in range(min_len,max_len+1):
    for j in product(char,repeat=i):
        word = "".join(word)
        file_open.write(word)
        file_open.write('\n')
        counter+1

print("Wordlist of {} paswords created ".format(counter))