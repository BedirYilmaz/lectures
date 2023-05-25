# guessing game with keyboard input
import os

target = 12
first_time = True

while True:

    if first_time:
        keyboard_input = int(input("please type in your guess. please use integers only.\n"))
        first_time = False
    else:
        keyboard_input = int(input("make another guess.\n"))
    os.system('clear')

    if keyboard_input > target:
        print("too large!")
    if keyboard_input < target:
        print("too small!")
    if keyboard_input == target:
        print("EXACTLY!!! YOU WON!!")
        break
