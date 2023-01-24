class Villager:
    def __init__(self, name):
        self.hp = 100
        self.attack = 5
        self.stamina = 100
        self.name = name
        
    def attack(self):
        if self.stamina <= 0:
            return
        self.stamina = self.stamina - 10
        if self.stamina < 0:
            self.stamina = 0
            
    def rest(self):
        self.stamina = 100
        
    def damage(self, hp_damage):
        self.hp = self.hp - hp_damage
        if self.hp <= 0:
            print("i am dead!")
            
    def speak(self):
        print("Hello my name is " + self.name)
        
class Knight(Villager):
    def __init__(self, name):
        self.hp = 150
        self.attack = 15
        self.stamina = 100
        self.name = name
        self.armor = 50
    
    def special(self):
        if self.stamina>= 50:
            self.stamina = self.stamina - 50
            
    def damage(self, hp_damage):
        if self.armor > 0:
            self.armor = self.armor - hp_damage
        else:
            self.hp = self.hp - hp_damage
            if self.hp <= 0:
                print("i am dead!")

if __name__ == "__main__":
    pad = Villager("pad")
    pad.speak()
    enzo = Knight("Zozo le rigolo")
    enzo.speak()
    