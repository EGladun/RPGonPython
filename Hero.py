import random as r


class Hero:
    """Class for creating of heroes"""
    allClasses = ["Knight", "Duelist", "Rogue", "Hunter", "Defender", "Druid", "Player", "Thief", "Morph"]
    heroClass = ""


    def __init__(self, name, race):
        """Constructor"""
        self.name = name
        self.race = race
        self.brutality = 1
        self.tactics = 1
        self.survivability = 1
        self.luck = 1
        self.statpoint = 1
        self.maxHealthPoints = 100

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
        print("brutality: ", self.brutality)
        print("tactics: ", self.tactics)
        print("survivability: ", self.survivability)
        print("Luck: ", self.luck)
        print("You have ", self.statpoint, " wild statpoints")
        if self.heroClass:
            print("Your class is", self.heroClass)

    def greeting(self):
        print("Hello, my name is", self.name)
        pass

    def statup(self, stat):
        if stat == 1:
            self.brutality += 1
            print("Brutality equals %d" % (self.brutality))
        elif stat == 2:
            self.tactics += 1
            print("Tactics equals %d" % (self.tactics))
        elif stat == 3:
            self.survivability += 1
            print("Survivability equals %d" % (self.survivability))
        else:
            print("Error stat")

    def topStat(self):
        if self.brutality > self.tactics and self.brutality > self.survivability and self.brutality > self.luck:
            return 1
        elif self.tactics > self.brutality and self.tactics > self.survivability and self.tactics > self.luck:
            return 2
        elif self.survivability > self.brutality and self.survivability > self.tactics and self.survivability > self.luck:
            return 3
        elif self.luck > self.brutality and self.luck > self.tactics and self.luck > self.survivability:
            return 4
        else:
            return 5
        
    def chooseHeroClass(self):
        predisposition = self.topStat()
        if predisposition == 1:
            print("You can choose %d or %d" %(self.allClasses[0], self.allClasses[1]))
            choose = input()
            if choose == 1:
                print("You choose %d class" %(self.allClasses[0]))
                self.heroClass = self.allClasses[0]
            elif choose == 2:
                print("You choose %d class" %(self.allClasses[1]))
                self.heroClass = self.allClasses[1]
            else:
                print("Wrong argument, retrying...")
                self.chooseHeroClass()
        elif predisposition == 2:
            print("You can choose %d or %d" %(self.allClasses[2], self.allClasses[3]))
            choose = input()
            if choose == 1:
                print("You choose %d class" %(self.allClasses[2]))
                self.heroClass = self.allClasses[2]
            elif choose == 2:
                print("You choose %d class" %(self.allClasses[3]))
                self.heroClass = self.allClasses[3]
            else:
                print("Wrong argument, retrying...")
                self.chooseHeroClass()
        elif predisposition == 3:
            print("You can choose %d or %d" %(self.allClasses[4], self.allClasses[5]))
            choose = input()
            if choose == 1:
                print("You choose %d class" %(self.allClasses[4]))
                self.heroClass = self.allClasses[4]
            elif choose == 2:
                print("You choose %d class" %(self.allClasses[5]))
                self.heroClass = self.allClasses[5]
            else:
                print("Wrong argument, retrying...")
                self.chooseHeroClass()
        elif predisposition == 4:
            print("You can choose %d or %d" %(self.allClasses[6], self.allClasses[7]))
            choose = input()
            if choose == 1:
                print("You choose %d class" %(self.allClasses[6]))
                self.heroClass = self.allClasses[6]
            elif choose == 2:
                print("You choose %d class" %(self.allClasses[7]))
                self.heroClass = self.allClasses[7]
            else:
                print("Wrong argument, retrying...")
                self.chooseHeroClass()
        elif predisposition == 5:
            print("You can choose only %d" %(self.allClasses[8]))
            self.heroClass = self.allClasses[8]
        print("Finally, you have a hero class - %d" %(self.heroClass))
            