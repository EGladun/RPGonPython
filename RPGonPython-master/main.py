from Hero import *
from JsonFiles import *

print("Write your hero's name")
hName = str(input())
print("Write your hero's race")
hRace = str(input())
hero = Hero(hName, hRace)
toJson(hero)


# hero.lvlup()
# hero.lvlup()
# toJson(hero)
# boomer = outJson("Hitnik")
# boomer.greeting()
