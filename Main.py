import os
import random
import sys

from Config import *

while True:

    # You're probably not supposed to do it this way, but this spits out True/False randomly
    yesorno = bool(random.choice([True, False]))
    has_ruins = yesorno

    # The variables from which these names and lists are loaded can be found in the configuration file

    no_ruins = var_no_ruins
    zone_ruins = var_zone_ruins
    ruin_monuments = var_ruin_monuments
    flavour_text = var_flavour_text
    rot_level = var_rot_level
    threats = var_threats
    threats_env = var_threats_env

    if has_ruins:
        a_list = random.sample(zone_ruins, 1)
        print("-Environment type-")
        print(a_list)
        c_list = random.sample(ruin_monuments, 1)
        print("-Ruin type present-")
        print(c_list)
        print("-Other information-")
        print("[Decide if ruin has Artefacts]")
    else:
        b_list = random.sample(no_ruins, 1)
        print("-Environment type-")
        print(b_list)
        print("-Mood elements present-")
        e_list = random.sample(flavour_text, 1)
        print(e_list)

    print("-Rot level for current zone-")
    d_list = random.sample(rot_level, 1)
    print("Rot level is " + str(d_list))

    choice = input("Would you like to regenerate environment? Yes - 1 No - 2 > ")
    choice = int(choice)

    if choice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
    elif choice == 2:
        sys.exit()
