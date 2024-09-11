from math import inf
def divide(first, second):
    if second:
        return first / second
    else:
        return (f'{inf} {'- Результат деления стремится к бесконечности'}')
