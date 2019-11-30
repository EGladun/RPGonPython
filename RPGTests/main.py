from heroClass import *

print("Hello, do you want to create new hero?")
newChecker = str(input())
if newChecker == "Yes" or "yes" or "Y" or "y":
    print("Write your hero's name")
    hName = str(input())
    print("Write your hero's race")
    hRace = str(input())
    hero = Hero(hName, hRace)
    pass
elif newChecker == "No" or "N" or "n" or "no":
    print("game is closed")
    pass
else:
    print("Uncnown command, repeat please")