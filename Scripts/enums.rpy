init -900 python:
    from enum import Enum, auto

    class DamageTypes(Enum):
        """|Enum|

        Типы урона
        """
        Crushing = auto() # 1 Дробящий
        Sound = auto() # 2 Звуковой
        Radiation = auto() # 3 Излучением
        Acid = auto() # 4 Кислотный
        Pricking = auto() # 5 Колющий
        Necrotic = auto() # 6 Некротический
        Fiery = auto() # 7 Огненный
        Mental = auto() # 8 Психический
        Chopping = auto() # 9 Рубящий
        Power = auto() # 10 Силовой
        Cold = auto() # 11 Холодом
        Electric = auto() # 12 Электрический
        Poisonous = auto() # 13 Ядом

    class States(Enum):
        """ |Enum|
        
        Состояния
        """
        Unconscious = auto() # 1 Бессознательный
        Scared = auto() # 2 Испуганый
        Invisible = auto() # 3 Невидимый
        Incapacitated = auto() # 4 Недееспособный
        Deafened = auto() # 5 Оглохший
        Petrified = auto() # 6 Окаменевший
        Entangled = auto() # 7 Опутанный
        Blinded = auto() # 8 Ослеплённый
        Poisoned = auto() # 9 Отравленный
        Charmed = auto() # 10 Очарованный
        Stunned = auto() # 11 Ошеломлённый
        Paralyzed = auto() # 12 Парализованный
        Knockout = auto() # 13 Сбитый с ног
        Captured = auto() # 14 Схваченный

#TODO Свериться с названиями оригинальной книги игрока