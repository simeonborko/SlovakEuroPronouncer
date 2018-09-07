from decimal import Decimal
import math


def pronounce(number: int) -> str:

    if number < 0 or number >= 1000000:
        raise Exception("Pronounce number must be between 0 and 999 999")

    if number == 1:
        eur = 'euro'
    elif 2 <= number <= 4:
        eur = 'eurá'
    else:
        eur = 'eur'

    return __pronounce(str(number)) + " " + eur


def pronounce_with_cents(n: Decimal) -> str:
    base = int(math.floor(n))
    rest = int(math.floor((n - base) * 100))
    eur = pronounce(base)
    if rest == 0:
        return eur
    elif rest == 1:
        return '{} a {} cent'.format(eur, rest)
    elif rest in (2, 3, 4):
        return '{} a {} centy'.format(eur, rest)
    else:
        return '{} a {} centov'.format(eur, rest)


def __pronounce(n: str) -> str:
    if len(n) == 1:
        return ('nula', 'jedno', 'dve', 'tri', 'štyri', 'päť', 'šesť', 'sedem', 'osem', 'deväť')[int(n)]

    elif len(n) == 2:
        if n[0] == '1':
            return ('desať', 'jedenásť', 'dvanásť', 'trinásť', 'štrnásť',
                    'pätnásť', 'šestnásť', 'sedemnásť', 'osemnásť', 'devätnásť')[int(n[1])]
        else:
            return ('', '', 'dvadsať', 'tridsať', 'štyridsať', 'päťdesiat', 'šesťdesiat', 'sedemdesiat',
                    'osemdesiat', 'deväťdesiat')[int(n[0])] + \
                   ('', 'jeden', 'dva', 'tri', 'štyri', 'päť', 'šesť', 'sedem', 'osem', 'deväť')[int(n[1])]

    elif len(n) == 3:
        return ('', 'sto', 'dvesto', 'tristo', 'štyristo', 'päťsto', 'šesťsto', 'sedemsto',
                'osemsto', 'deväťsto')[int(n[0])] + __pronounce(n[1:])

    elif len(n) == 4:
        if n[0] == '0':
            raise Exception
        return ('', 'tisíc', 'dvetisíc', 'tritisíc', 'štyritisíc', 'päťtisíc', 'šesťtisíc', 'sedemtisíc',
                'osemtisíc', 'deväťtisíc')[int(n[0])] + __pronounce(n[1:])

    elif len(n) == 5:
        if n[0] == '0':
            raise Exception
        return __pronounce(n[:2]) + 'tisíc' + __pronounce(n[2:])

    elif len(n) == 6:
        if n[0] == '0':
            raise Exception
        return __pronounce(n[:3]) + 'tisíc' + __pronounce(n[3:])
