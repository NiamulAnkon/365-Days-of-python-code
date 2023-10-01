#Basic Chatbot
import random
greetings = ["hello", "hi", "yo", "hey", "heyo", "ei"]
greetings_responses = ["hey there", "hello", "hi", "yse!", "yo! how are you?",]

def chatbot(user_input):
  user_input = user_input
  
  if user_input in greetings:
      return random.choice(greetings_responses)

  elif user_input == "how are you":
    return "otto: i am good! and you?"

  elif user_input == "give me some idea":
    return "Otto: i can't because i am not peanut :)"

  elif user_input == "i am good too":
    return "ok"

  elif user_input == "good":
    return "ok :)"
    
  elif user_input == "bye": 
      return "otto: GoodBye"

  else:
    print("otto: Sorry i am a simple chatbot i can't answear this")

  
print("OTTO: Hello my name is otto how can i help you (type bye to exit)")

while True:
  user_input = input("You: ")

  if user_input == "bye":
    print("Otto: GoodBye :)")
    break

  bot = chatbot(user_input)
  print("Otto: ", bot)