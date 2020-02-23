import random as r
from math import *


class Hero:
    """Class for creating of heroes"""

    def __init__(self, name, race):
        """Constructor"""
        self.name = name
        self.race = race
        self.brutality = 1
        self.tactics = 1
        self.survivability = 1
        self.luck = 1
        self.statpoint = 1

        print("Welcome to Underworld, ", race, ", ", name)
        print("Your stats is:")
        print("brutality: ", self.brutality)
        print("tactics: ", self.tactics)
        print("survivability: ", self.survivability)
        print("luck: ", self.luck)
        print("You have ", self.statpoint, " wild statpoints")

    def checkStats(self):
        print("Your stats is:")
        print("Max HP: ", self.maxHealthPoints)
        print("Max MP: ", self.maxManaPoints)
        print("brutality: ", self.brutality)
        print("tactics: ", self.tactics)
        print("survivability: ", self.survivability)
        print("Luck: ", self.luck)
        print("You have ", self.statpoint, " wild statpoints")

    def crit(self):
        if (r.randrange(0, 100, 1)) <= self.critChance:
            return True
        else:
            return False

    def greeting(self):
        print("Hello, my name is", self.name)
        pass

    def statsUp(self, stat):
        self.brutality += stat
        self.tactics += stat
        self.survivability += stat
        self.luck += stat
        print("Все статы увеличены на ", stat)

    def lvlup(self):
        self.exp = 0
        self.lvl += 1
        self.statpoint += 1
        print("Уровень игрока ", self.name, " повышается...")
        print("теперь ваш уровень равен ", self.lvl)
        print("Вы получаете 1 очкo характеристик, у вас ", self.statpoint, "нераспределенных очков характеристик")
        self.checkStats()
