import random as r
from math import *

class Hero:
    """Class for creating of heroes"""
 
    def __init__(self, name, race):
        """Constructor"""
        self.name = name
        self.race = race
        self.strength = r.randrange(1,8,1)
        self.endurance = r.randrange(1,8,1)
        self.agility = r.randrange(1,8,1)
        self.intellect = r.randrange(1,8,1)
        self.luck = r.randrange(1,10,1)
        self.karma = 0
        self.weaponDamage = r.randrange(4,8,1)
        self.critChance = ceil(self.agility*0.1)
        self.lvl = 1
        self.statpoint = 3
        self.exp = 0
        self.bonusHP = 10
        self.bonusMP = 0
        self.combatDamage = 0

        if self.race == "Orc":
            self.strength += 2
            self.agility += 1
            self.intellect -= 3
            self.bonusHP = 20
            if self.intellect <= 0:
                self.intellect = 1
                pass
            pass
        elif self.race == "Elf":
            self.agility += 2
            self.intellect += 1
            self.strength -= 3
            self.bonusMP = 5
            if self.strength <= 0:
                self.strength = 1
                pass
            self.endurance -= 2
            pass
        elif self.race == "Tifling":
            self.intellect += 2
            self.strength += 1
            self.agility -= 3
            self.bonusMP = 10
            if self.agility <= 0:
                self.agility = 1
                pass
            pass
        elif self.race == "Human":
            self.luck += 2
            self.agility += 1
            self.endurance -= 1
            self.bonusHP = 15
            pass

        if self.endurance <= 2:
            self.endurance = 3
            pass

        self.maxHealthPoints = self.endurance * 10 + self.bonusHP
        self.maxManaPoints = self.intellect * 10 + self.bonusMP
        
        print("Welcome to Underworld, ", race, ", ", name)
        print("Your stats is:")
        print("Max HP: ", self.maxHealthPoints)
        print("Max MP: ", self.maxManaPoints)
        print("Strength: ", self.strength)
        print("Endurance: ", self.endurance)
        print("Agility: ", self.agility)
        print("Intellect: ", self.intellect)
        print("Luck: ", self.luck)
        print("You have ", self.statpoint, " wild statpoints")
        pass
    
    def checkStats(self):
        print("Your stats is:")
        print("Max HP: ", self.maxHealthPoints)
        print("Max MP: ", self.maxManaPoints)
        print("Strength: ", self.strength)
        print("Endurance: ", self.endurance)
        print("Agility: ", self.agility)
        print("Intellect: ", self.intellect)
        print("Luck: ", self.luck)
        print("You have ", self.statpoint, " wild statpoints")
        pass

    def crit(self):
            if ((r.randrange(0,100,1)) <= self.critChance):
                return True
                pass
            else:
                return False
                pass
    pass

    def punch(self):
        self.critChance = ceil(self.agility*0.1)
        self.combatDamage = ceil(self.strength/2 + self.weaponDamage)
        self.crit()
        if self.crit() == True:
            print("Критический урон!!! Вы наносите ", self.combatDamage*2, " урона!")
            pass
        else:
            print("Ваш удар наносит ", self.combatDamage, " урона")
            pass
    pass

    def greeting(self):
        print("Hello, my name is ", self.name)
        pass

    def statsUp(self, stat):
        self.strength += stat
        self.endurance += stat
        self.agility += stat
        self.intellect += stat
        self.luck += stat
        print("Все статы увеличены на ", stat)
        pass

    def lvlup(self):
        self.exp = 0
        self.lvl += 1
        self.statpoint += 3
        self.bonusHP += self.bonusHP
        self.bonusMP += self.bonusMP
        self.maxHealthPoints = self.endurance * 10 + self.bonusHP
        self.maxManaPoints = self.intellect * 10 + self.bonusMP
        self.statsUp(1)
        print("Уровень игрока ", self.name, " повышается...")
        print("теперь ваш уровень равен ", self.lvl)
        print("Вы получаете 3 очка характеристик, теперь у вас ", self.statpoint, " нераспределенных очков характеристик")
        self.checkStats()
        pass