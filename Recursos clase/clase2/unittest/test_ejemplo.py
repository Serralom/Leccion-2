# .assertEqual(a, b): Verifica la igualdad de ambos valores.
# .assertTrue(x): Verifica que el valor es True.
# .assertFalse(x): Verifica que el valor es False.
# .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
# .assertIsNone(x): Verifica que el valor es None.
# .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
# .assertIsInstance(a, b): Verifica que a es una instancia de b
# .assertRaises(x): Verifica que se lanza una excepción.

import unittest

class TestEjemplosU(unittest.TestCase):
    def test_in(self):
        self.assertIn(4,[5,6,3])
    
    def test_is(self):
        a = [1,2,3]
        b = [4]
        self.assertIs(a,b)
    
    def test_excepcion(self):
        with self.assertRaises(ZeroDivisionError):
            x = 0/0
        