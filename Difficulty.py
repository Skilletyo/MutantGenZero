import os
import random

while True:
    choice = input("Please choose a Threat Level between 1 - 3 > ")
    choice = int(choice)

    if choice == 1:
        difficulty = random.randint(1, 4)
        print("Threat level is " + str(difficulty))
    elif choice == 2:
        difficulty = random.randint(5, 8)
        print("Threat level is " + str(difficulty))
    elif choice == 3:
        difficulty = random.randint(9, 14)
        print("-Threat level is " + str(difficulty), "-")

    for i in range(difficulty):
        num = random.randint(1, 6)
        if num == 6:
            print("Artefact found!")
        if num == 1:
            print("Threat found!")

    input("Please press enter if you want to reroll! ")
    os.system('cls' if os.name == 'nt' else 'clear')
