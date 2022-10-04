from operaciones import *
import unittest

class TestCalculoMedia(unittest.TestCase):
    def test_1(self):
        resultado = calculo_media([5,5,5,5])
        self.assertEqual(resultado,5)
    
    
    def test_2(self):
        resultado = calculo_media([10,10,10])
        self.assertEqual(resultado,10)
    
if __name__ == '__main__':
    unittest.main()
