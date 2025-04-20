import random

def random_rcp():
    rock_sci_paper=["가위","바위","보"]
    computer=random.choice(rock_sci_paper)
    return computer

def compare(player,com):
    if player=="가위":
        if com=="가위":
            print("Draw")
        elif com=="바위":
            print("Lose")
        else: 
            print("Win")
            return 1
    if player=="바위":
        if com=="가위":
            print("Win")
            return 1
        elif com=="바위":
            print("Draw")
        else: 
            print("Lose")
    if player=="보":
        if com=="가위":
            print("Lose")
        elif com=="바위":
            print("Win")
            return 1
        else: 
            print("Draw")
    return 0
    