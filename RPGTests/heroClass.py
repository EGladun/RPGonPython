import random as r

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

        if self.race == "Orc":
            self.strength += 2
            self.agility += 1
            self.intellect -= 3
            if self.intellect <= 0:
                self.intellect = 1
                pass
            pass
        elif self.race == "Elf":
            self.agility += 2
            self.intellect += 1
            self.strength -= 3
            if self.strength <= 0:
                self.strength = 1
                pass
            self.endurance -= 2
            pass
        elif self.race == "Tifling":
            self.intellect += 2
            self.strength += 1
            self.agility -= 3
            if self.agility <= 0:
                self.agility = 1
                pass
            pass
        elif self.race == "Human":
            self.luck += 2
            self.agility += 1
            self.endurance -= 1
            pass

        if self.endurance <= 2:
            self.endurance = 3
            pass

        self.maxHealthPoints = self.endurance * 10
        self.maxManaPoints = self.intellect * 10
        
        print("Welcome to Underworld, ", race, ", ", name)
        print("Your stats is:")
        print("Max HP: ", self.maxHealthPoints)
        print("Max MP: ", self.maxManaPoints)
        print("Strength: ", self.strength)
        print("Endurance: ", self.endurance)
        print("Agility: ", self.agility)
        print("Intellect: ", self.intellect)
        print("Luck: ", self.luck)
        pass
