import pywhatkit as pwk
txt = '''In this Python handwriting project, you will learn how to convert 
text to handwriting. It is a  tbasic project
hat will help you with
a better understanding of Python.'''

pwk.text_to_handwriting(txt, "demo1.png", [0,0,138])
print("End")
