# def capital_case(x):
#     return x.capitalize()


def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("No has utilizado una cadena")
    return x.capitalize()