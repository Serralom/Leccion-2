from operaciones import suma
from operaciones import resta

def test_suma():
    assert suma(2,2) == 4

def test_resta():
    assert resta(5,2) == 3