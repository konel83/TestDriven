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
        wynik = kalkulator.add('a',5)
        self.assertEqual(wynik, False)

    def test_add_6(self):
        wynik = kalkulator.add(5,'a')
        self.assertEqual(wynik, False)

    def test_add_7(self):
        wynik = kalkulator.add(5.01,0.01)
        self.assertEqual(wynik, 5.02)

    def test_add_8(self):
        wynik = kalkulator.add(987654321,123456789)
        self.assertEqual(wynik, 1111111110)

    def test_add_9(self):
        wynik = kalkulator.add(1,2,3)
        self.assertEqual(wynik, 6)

    def test_sub_1(self):
        wynik = kalkulator.sub(5,5)
        self.assertEqual(wynik, 0)

    def test_sub_2(self):
        wynik = kalkulator.sub(-5,5)
        self.assertEqual(wynik, -10)

    def test_sub_3(self):
        wynik = kalkulator.sub(-5,-5)
        self.assertEqual(wynik, 0)

    def test_sub_4(self):
        wynik = kalkulator.sub('a','a')
        self.assertEqual(wynik, False)

    def test_sub_5(self):
        wynik = kalkulator.sub('a',5)
        self.assertEqual(wynik, False)

    def test_sub_6(self):
        wynik = kalkulator.sub(5,'a')
        self.assertEqual(wynik, False)

    def test_sub_7(self):
        wynik = kalkulator.sub(5.01,0.01)
        self.assertEqual(wynik, 5.00)

    def test_sub_8(self):
        wynik = kalkulator.sub(987654321,123456789)
        self.assertEqual(wynik, 864197532)

    def test_mul_1(self):
        wynik = kalkulator.mul(5,5)
        self.assertEqual(wynik, 25)

    def test_mul_2(self):
        wynik = kalkulator.mul(0,5)
        self.assertEqual(wynik, 0)

    def test_mul_3(self):
        wynik = kalkulator.mul(5,0)
        self.assertEqual(wynik, 0)

    def test_mul_4(self):
        wynik = kalkulator.mul(0,0)
        self.assertEqual(wynik, 0)

    def test_mul_5(self):
        wynik = kalkulator.mul(-1,5)
        self.assertEqual(wynik, -5)

    def test_mul_6(self):
        wynik = kalkulator.mul(3,-6)
        self.assertEqual(wynik, -18)

    def test_mul_7(self):
        wynik = kalkulator.mul(-8,-8)
        self.assertEqual(wynik, 64)

    def test_mul_8(self):
        wynik = kalkulator.mul('a',-8)
        self.assertEqual(wynik, False)

    def test_mul_9(self):
        wynik = kalkulator.mul(5, 'a')
        self.assertEqual(wynik, False)

    def test_mul_10(self):
        wynik = kalkulator.mul('a', 'a')
        self.assertEqual(wynik, False)

    def test_mul_11(self):
        wynik = kalkulator.mul(3.5,2)
        self.assertEqual(wynik, 7)

    def test_mul_12(self):
        wynik = kalkulator.mul(1.5,1.5)
        self.assertEqual(wynik, 2.25)

    def test_div_1(self):
        wynik = kalkulator.div(5,5)
        self.assertEqual(wynik, 1)

    def test_div_2(self):
        wynik = kalkulator.div(1,5)
        self.assertEqual(wynik, 0.2)

    def test_div_3(self):
        wynik = kalkulator.div(5,0)
        self.assertEqual(wynik, False)

    def test_div_4(self):
        wynik = kalkulator.div(1,1)
        self.assertEqual(wynik, 1)

    def test_div_5(self):
        wynik = kalkulator.div(0,0)
        self.assertEqual(wynik, False)

    def test_div_6(self):
        wynik = kalkulator.div(-1,1)
        self.assertEqual(wynik, -1)

    def test_div_7(self):
        wynik = kalkulator.div(-5,3)
        self.assertEqual(wynik, -5/3)


if __name__ == '__main__':
    unittest.main()
