import json
from RPGTests.Hero import *

def toJson(hero):
    main_hero = {
        "name": hero.name,
        "race": hero.race,
        "exp": hero.exp,
        "lvl": hero.lvl,
        "maxHP": hero.maxHealthPoints,
        "maxMP": hero.maxManaPoints,
        "statpoints": hero.statpoint,
        "bonusHP": hero.bonusHP,
        "bonusMP": hero.bonusMP,
        "strength": hero.strength,
        "endurance": hero.endurance,
        "agility": hero.agility,
        "intellect": hero.intellect,
        "luck": hero.luck
    }

    file = "heroes/" + str(hero.name) + "-file.json"
    with open(file, "w") as write_file:
        json.dump(main_hero, write_file, indent=4)
    print("Json is created with name ", file)
    pass


def outJson(name):
    file = "heroes/" + str(name) + "-file.json"
    if file:
        with open(file, "r") as read_file:
            data = json.load(read_file)
            new_hero = Hero()
            new_hero.name = data['name']
            new_hero.race = data['race']
            new_hero.exp = data['exp']
            new_hero.lvl = data['lvl']
            new_hero.maxHealthPoints = data['maxHP']
            new_hero.maxManaPoints = data['maxMP']
            new_hero.statpoint = data['statpoints']
            new_hero.bonusHP = data['bonusHP']
            new_hero.bonusMP = data['bonusMP']
            new_hero.strength = data['strength']
            new_hero.endurance = data['endurance']
            new_hero.agility = data['agility']
            new_hero.intellect = data['intellect']
            new_hero.luck = data['luck']
            return new_hero
    else:
        print("Нет файла с таким именем")