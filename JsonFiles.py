import json
from Hero import *


def toJson(hero):
    main_hero = {
        "name": hero.name,
        "race": hero.race,
        "statpoint": hero.statpoint,
        "brutality": hero.brutality,
        "tactics": hero.tactics,
        "survivability": hero.survivability,
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
            new_hero = Hero(data['name'], data['race'])
            new_hero.exp = data['exp']
            new_hero.lvl = data['lvl']
            new_hero.statpoint = data['statpoint']
            new_hero.brutality = data['brutality']
            new_hero.tactics = data['tactics']
            new_hero.survivability = data['survivability']
            new_hero.luck = data['luck']
            return new_hero
    else:
        print("Нет файла с таким именем")
