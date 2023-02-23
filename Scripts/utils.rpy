init -999 python:
    from random import randint
    import re

    def roll_dice(formula: str):
        replacer = re.compile("\d*d\d+")

        while True:
            if (enter := re.search(replacer, formula)) is None:
                break
            
            count, sides = map(int, enter[0].split('d'))

            count = 1 if count == '' else count

            formula = formula.replace(enter[0], randint(count, sides * count))

        return eval(formula)
