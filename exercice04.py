class Villager:
    def __init__(self, name):
        self.hp = 100
        self.attack = 5
        self.stamina = 100
        self.name = name
    

if __name__ == "__main__":
    pad = Villager("pad")
    print(pad.hp)
    pad.hp = 50
    print(pad.hp)
    