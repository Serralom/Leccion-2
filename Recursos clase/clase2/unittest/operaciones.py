from ast import arg


def calculo_media(*args):
    return (sum(*args)/len(*args))


# print(calculo_media([3,5,7]))

# assert(calculo_media([3,5,7]) == 5.0)