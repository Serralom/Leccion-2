import unittest

class TestEjemplosU(unittest.TestCase):

    def test_1(self):
        resultado = calculo_media(4,[5,6,3,4])
        self.assertEqual(resultado,10)

    def test_is(self):
        a = [1,2,3]
        b = a
        self.assertIs(a,b)

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            x = 0/0