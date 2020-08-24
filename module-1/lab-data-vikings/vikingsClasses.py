
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

    

# Saxon


class Saxon (Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    

# War

import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        vikingSoldier = random.choice(self.vikingArmy)
        saxonSoldier = random.choice(self.saxonArmy)
        saxonSoldier.receiveDamage(vikingSoldier.attack())
        if saxonSoldier.health <=0:
            self.saxonArmy.remove(saxonSoldier)
        return f"result of calling {vikingSoldier.attack()} of a Saxon with the strength of a Viking"

    def saxonAttack(self):
        vikingSoldier = random.choice(self.vikingArmy)
        saxonSoldier = random.choice(self.saxonArmy)
        vikingSoldier.receiveDamage(saxonSoldier.attack())
        if vikingSoldier.health <=0:
            self.vikingArmy.remove(vikingSoldier)
        return f"result of calling {saxonSoldier.attack()} of a {vikingSoldier} with the strength of a Saxon"

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)==1 and len(self.vikingArmy)==1:
            return "Vikings and Saxons are still in the thick of battle."
    
    '''
    def saxonAttack(self):
        vikingSoldier = random.choice(self.vikingArmy)
        saxonSoldier = random.choice(self.saxonArmy)
        vikingSoldier.receiveDamage(saxonSoldier.attack())
        if vikingSoldier.health <=0:
            self.vikingArmy.remove(vikingSoldier)
        return f"result of calling {saxonSoldier.attack()} of a Viking with the strength of a Saxon"

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)==1 and len(self.vikingArmy)==1:
            return "Vikings and Saxons are still in the thick of battle."
    '''