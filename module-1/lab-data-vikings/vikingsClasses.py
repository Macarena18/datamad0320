
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health-=damage


# Viking

class Viking(Soldier):
    def __init__(self,name,health,strenght):
        super().__init__(health,strenght)
        self.name = name

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
           return f"{self.name} has received {damage} points of damage"
        else:
           return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return f"Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        
    def addViking(self,Viking):
         self.vikingArmy.append(Viking)
            
    def addSaxon(self,Saxon):
         self.saxonArmy.append(Saxon)
            
    def vikingAttack(self):
        s_saxon=random.choice(self.saxonArmy)
        s_viking=random.choice(self.vikingArmy)
        attack=s_saxon.receiveDamage(s_viking.attack())
        if s_saxon.health<=0:
            self.saxonArmy.remove(s_saxon)
        return attack
        
    def saxonAttack(self):
        s_saxon=random.choice(self.saxonArmy)
        s_viking=random.choice(self.vikingArmy)
        attack2=s_viking.receiveDamage(s_saxon.attack())
        if s_viking.health<=0:
            self.vikingArmy.remove(s_viking)
        return attack2
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."
    

