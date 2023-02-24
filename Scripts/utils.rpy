init -999 python:
    from random import randint
    import re

    def roll_dice(formula: str):
        """
            Бросает дайсы и возвращает значение по формуле

            formula: str - Математическое выражение содержащее нотацию броска в виде [количество дайсов]d<количество граней>
        """
        replacer = re.compile("\d*d\d+")

        while True:
            if (enter := re.search(replacer, formula)) is None:
                break
            
            count, sides = map(int, enter[0].split('d'))

            count = 1 if count == '' else count # Если количество дайсов не указано, то считается, что бросается один дайс

            formula = formula.replace(enter[0], randint(count, sides * count)) # Заменяем нотацию на число

        return eval(formula) # Выполняем выражение
