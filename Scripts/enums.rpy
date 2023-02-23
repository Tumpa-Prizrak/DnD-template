init -900 python:
    from enum import Enum, auto

    class DamageTypes(Enum):
        Crushing = auto() # 1
        Sound = auto() # 2
        Radiation = auto() # 3
        Acid = auto() # 4
        Pricking = auto() # 5
        Necrotic = auto() # 6
        Fiery = auto() # 7
        Mental = auto() # 8
        Chopping = auto() # 9
        Power = auto() # 10
        Cold = auto() # 11
        Electric = auto() # 12
        Poisonous = auto() # 13
