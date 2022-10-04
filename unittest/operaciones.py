def calculo_media(*args):
    return(sum(*args)/len(*args))

print (calculo_media([2,4,6,8]))

assert(calculo_media([2,4,6,8]) == 5)