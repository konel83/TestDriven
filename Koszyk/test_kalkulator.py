#test_program.def
#imort modulu unittest():
import unittest

#import modulu (obiekt testowy()
import kalkulator

class TestProgram(unittest.TestCase):
    def test_add_1(self):
        wynik = kalkulator.add(5,5)
        self.assertEqual(wynik, 10)

    def test_add_2(self):
        wynik = kalkulator.add(-5,5)
        self.assertEqual(wynik, 0)

    def test_add_3(self):
        wynik = kalkulator.add(-5,-5)
        self.assertEqual(wynik, -10)

    def test_add_4(self):
        wynik = kalkulator.add('a','a')
        self.assertEqual(wynik, False)

    def test_add_5(self):
        wynik = kalkulator.add('a','5')
        self.assertEqual(wynik, False)

    def test_add_6(self):
        wynik = kalkulator.add('5','a')
        self.assertEqual(wynik, False)

    def test_add_7(self):
        wynik = kalkulator.add(5.01,0.01)
        self.assertEqual(wynik, 5.02)

    def test_sub(self):
        wynik = kalkulator.sub(5,5)
        self.assertEqual(wynik, 0)

    def test_mul(self):
        wynik = kalkulator.mul(5,5)
        self.assertEqual(wynik, 25)

    def test_div(self):
        wynik = kalkulator.div(5,5)
        self.assertEqual(wynik, 1)

if __name__ == '__main__':
    unittest.main()
