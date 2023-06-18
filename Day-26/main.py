def encode(message):

  if len(message) >= 3:
    firstLetter = message[0]
    message = message[1:] + firstLetter
    code = "" + message + "."

  else:
    code = message[::-1]

  return code


def decode(code):

  if len(code) < 3:
    message = code[::-1]

  elif code.startswith("") and code.endswith("."):
    message = code[3:-3]
    lastLetter = message[-1]
    message = lastLetter + message
  else:
    message = code

  return message


message = input("Write a message : ")
answer = input("You want to encode the code or decode the code? type ec or dc: ")

if (answer == "ec"):
  code = encode(message)
  print("Encoded message is ", code)
elif (answer == "dc"):
  messaged = decode(message)
  print("Decoded message is ", messaged)
else:
  print("Invalid input. Choose from 'encode' or 'decode' only")