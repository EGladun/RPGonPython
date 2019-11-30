from heroClass import *

print("Write your hero's name")
hName = str(input())
print("Write your hero's race")
hRace = str(input())
hero = Hero(hName, hRace)
hero.punch()
