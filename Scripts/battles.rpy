init python:
    class Attack:
        def __init__(self, name: str, attack_bonus: int, damage: int, damage_type: DamageTypes):
            self.name = name
            self.attack_bonus = attack_bonus
            self.damage = damage
            self.damage_type = damage_type
        
        def attack(self):
            pass

    class Entity:
        def __init__(self, name: str, token: str, hp: int, speed: int, ac: int, initiative_bonus: int):
            self.name = name
            self.token = token
            self.hp = hp
            self.speed = speed
            self.ac = ac
            self.initiative_bonus = initiative_bonus
            
            self.states = []
