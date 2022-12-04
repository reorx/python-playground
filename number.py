
def round_to_int(n):
    if n < 0:
        return int(n - 0.5)
    return int(n + 0.5)


def round2(n):
    return round_to_int(n * 100) / 100.0


def round3(n):
    return round_to_int(n * 1000) / 1000.0


## Decimal


from decimal import Decimal as D


def round_str(number, precision=3):
    if number == '':  # XXX
        return number

    if isinstance(number, str):
        return str(round(D(number), precision))
    elif isinstance(number, D):
        return str(round(number, precision))
    elif isinstance(number, int):
        return str(round(D(number), precision))
    elif isinstance(number, float):
        return str(round(D(str(number)), precision))
    else:
        raise TypeError('Unsupported number type: {}'.format(type(number)))


def to_decimal(number):
    if isinstance(number, float):
        return D(str(number))
    elif isinstance(number, str):
        return D(number)
    elif isinstance(number, int):
        return D(number)
    elif isinstance(number, D):
        return number
    else:
        raise TypeError('Unsupported number type: {}'.format(type(number)))
