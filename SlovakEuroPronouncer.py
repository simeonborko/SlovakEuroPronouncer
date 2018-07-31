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
        if n[0] == '0':
            raise Exception
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
