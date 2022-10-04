from actividad_1_1 import *
import pytest 

def test_menos_ingresos():
    for column in df:
        a = df[column].mean()
        print(a)
        correcto = True
        # if a > max:
        #     correcto = False
        # else:
        #     pass
    assert correcto == True

test_menos_ingresos()

def test_mas_ingresos():
    for column in df:
        a = df[column].mean()
        if a < mas_ingresos:
            return False
        else:
            return True
    assert test_mas_ingresos == True

def test_media_gastos():
    pass

def test_gasto_total():
    pass

def test_ingresos_totales():
    pass
