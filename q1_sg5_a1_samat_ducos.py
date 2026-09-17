9 - Samat
21 - Ducos, Janine Chrisha M.

class Hero:
    def __init__ (self, name, hp):
        self.name = name
        self.hp = hp
    
    def health(self, amount):
        self.hp -= amount
    
Arthur = Hero("Arthur", 100)
Morgana = Hero("Morgana", 100)

Arthur.health(10)
    
print(Arthur.name, "has taken", Arthur.hp, "damage")
print(Morgana.name, "has taken", Morgana.hp, "damage")
