import os
import time
import random

def clear():
    os.system("cls")

def miner():
    x = random.randint(1, 100)
    clear()
    print "mining."
    time.sleep(1.5)
    clear()
    print "mining.."
    time.sleep(1.5)
    clear()
    print "mining..."
    time.sleep(1.5)
    clear()
    print "+" +str(x)+ " gold!"
    time.sleep(1.5)
    clear()
    return(x)

def helper():
    print("commands: \n\tmine : mine some gold \n\tgold: show gold balance\n\texit: close the program")
    print("\n\thelp: shows this list\n\tclear: clears the mining console")

gold = 0
print("\t\tWelcome to gold mining simulator")
print("\tThe most boring game on the planet")
helper()

while True:
    command = raw_input("miner: ")

    if command == "mine":
        x = miner()
        gold = gold + x
    elif command == "gold":
        print("gold: " + str(gold))
    elif command == "help":
        helper()
    elif command == "clear":
        clear()
    elif command == "exit":
        break
