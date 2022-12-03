import math
import random
import time

print("")
print("     Welcome to praise and")
print("        Self Compassion!")
print("    Created by Spencer Boggs")
print("")
input("    Press [Enter] to Start")
while True:
    print("")
    name = input("Your name: ")
    print("")

    insults = [
        "You are an intelligent individual.",
        name + ", you are a pitiful \n excuse for a human being", 
        "Gek", 
        "Protozoan", 
        "More of your conversation\n would infect my brain.", 
        "You, minion, are too saucy.", 
        "I do wish thou were a dog,\n that I might love thee\n something.",
        "Why am I wasting my battery\n talking to you...",
        "Theres a reason you don't\n love yourself",
        "You are missing a chromosome",
        "I swear to God, I'm going to\n boil your teeth",
        "I'm going to rip your vocal\n chords out and use them\n as shoelaces.",
        "Your existance is completely\n meaningless. All you do is\n contribute to the heat death\n of the universe.",
        "No bitches."]

    if (name == "no"):
        print("Liar. Thats not your name")
    elif (name):
        print("  Hello, " + name)
        while (len(insults) > 0):
            rand = random.randint(0,len(insults)-1)
            print("")
            if (rand == 0) and (insults[0] == "You are an intelligent individual."):
                print(" " + insults[rand])
                time.sleep(1)
                print(" Just kidding. I lied")
                insults.pop(rand)
            else:
                print(" " + insults[rand])
                insults.pop(rand)
            print("")
            input("  Press [Enter] for more")

    
        print("")
        print("  You aren't even worth any more words.")
        input("")
        print("")
        print("  You can leave now")
        input("")
        print("")
        print("  Bye")
        input("")
        print("")
        print("  Get the fuck out")
    else:
        print("Fuck you. You little bitch.")
        print("Enter your name now!")