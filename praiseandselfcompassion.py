import math
import random

print("")
print("     Welcome to praise and")
print("        Self Compassion!")
print("    Created by Spencer Boggs")
print("")
input("    Press [Enter] to Start")
while True:
    print("")
    name = input("Please enter your name: ")
    print("")

    insults = [
        name + ", you are a pitiful excuse for a human being", 
        "Gek", 
        "Protozoan", 
        "More of your conversation would infect my brain.", 
        "You, minion, are too saucy.", 
        "I do wish thou were a dog, that I might love thee something.",
        "Why am I wasting my battery talking to you..."]

    if (name.casefold() == "no"):
        print("Liar. Thats not your name")
    elif (name):
        print("  Hello, " + name)
        for x in insults:
            rand = random.randint(0,len(insults)-1)
            print("")
            print("  " + insults[rand])
            insults.pop(rand)
            print("")
            input("  Press [Enter] for next compliment")
        print("")
        print("  You aren't even worth any more words.")
    else:
        print("Fuck you. You little bitch.")
        print("Enter your name now!")