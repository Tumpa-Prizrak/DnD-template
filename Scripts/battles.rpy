init python:
    class Attack:
        """
        Репрезентация атаки персонажа или NPC

            name: str - Название атаки
            attack_bounts: int - Бонус к броску на попадание
            damage: str - формула или число наносимого урона
            damage_type: DamageTypes - Тип урона
        """
        def __init__(self, name: str, attack_bonus: int, damage: str, damage_type: DamageTypes):
            self.name = name
            self.attack_bonus = attack_bonus
            self.damage = damage
            self.damage_type = damage_type
        
        def attack(self):
            pass

    class Entity:
        """
        Репрезентация персонажа или NPC

            name: str - Имя персонажа или NPC
            token: str - Путь к изображению репрезентирующему персонажа на поле
            speed: int - Скорость персонажа в футах
            ac: int - Класс доспеха или КД
            initiative_bonus - Число, которое прибовляется при броске инициативы
            hp: int - Текущее количество очков здоровья
            max_hp: int - Максимальное количество очков здоровья
        """
        def __init__(self, name: str, token: str, speed: int, ac: int, initiative_bonus: int, hp: int, max_hp: int = None):
            self.name = name
            self.token = token
            self.speed = speed
            self.ac = ac
            self.initiative_bonus = initiative_bonus
            
            self.hp = hp
            self.max_hp = hp if max_hp is None else max_hp


            self.states = []
