#modul pravi tokene od izraza
import re

__author__ = 'mijicd'

REGEX = r'(?:\d*\.\d+)|(?:\d+)|(?:[()+\-\^/*])'

#greska ako izraz nije dat kao string
class ExpressionNotStringError(Exception):
    pass

#greska ako izraz sadrzi nevalidne znakove
class UnknownCharacterError(Exception):
    pass

#funkcija kreira tokene na osnovu zadatog izraza, vraca listu tokena
def tokenize(expression):
    """Postupak formiranja liste tokena koristi regularni izraz
    zadat putem REGEX varijable. Omogućeno je pronalaženje
    sledećih tipova tokena:
        - floating-point vrednosti
        - celobrojne vrednosti
        - operatori +, -, *, /, ^
        - zagrade
    """
    #greska ako izraz nije dat kao string
    if not isinstance(expression, str):
        raise ExpressionNotStringError("Izraz treba da bude dat kao string")

    #pravljenje tokena
    tokens = re.findall(REGEX, expression)

    #greska ako izraz sadrzi nevalidne znakove
    if expression.replace(" ", "") != "".join(tokens):
        raise UnknownCharacterError("Izraz sadrzi nevalidne znakove")

    return tokens

if __name__ == '__main__':
    pass