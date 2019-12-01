from heroClass import *
import json

#print("Write your hero's name")
hName = str(input())
#print("Write your hero's race")
hRace = str(input())
hero = Hero(hName, hRace)
def toJson():
    mainHero = {
    "name":hero.name,
    "race":hero.race,
    "exp":hero.exp,
    "lvl":hero.lvl,
    "maxHP":hero.maxHealthPoints,
    "maxMP":hero.maxManaPoints,
    "bonusHP":hero.bonusHP,
    "bonusMP":hero.bonusMP,
    "strength":hero.strength,
    "endurance":hero.endurance,
    "agility":hero.agility,
    "intellect":hero.intellect,
    "luck":hero.luck
    }

    file = str(hero.name) + "-file.json"
    with open(file, "w") as write_file:
        json.dump(mainHero, write_file)
    pass

hero.lvlup()
hero.lvlup()
toJson()