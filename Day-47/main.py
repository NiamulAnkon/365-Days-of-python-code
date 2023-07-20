#exercise
#Write a Python function called reverse_words that takes a sentence as input and returns the sentence with each word reversed. Words are separated by spaces, and there are no punctuation marks.

def reversed_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

try:
    # Example sentence
    sentence = input("Enter any sentence: ")
    result = reversed_words(sentence)
    print(result)
except ValueError:
    print("Something Went Wrong")
