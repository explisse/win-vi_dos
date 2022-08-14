import keyboard


b = input("number of desktop (i = infinity): ")

if b == "i":
    while True:
        keyboard.press_and_release("ctrl+win+d")
        a=a+1
else:
    a=0
    while a < int(b):
        keyboard.press_and_release("ctrl+win+d")
        a=a+1