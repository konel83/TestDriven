#test_program.def
#imort modulu unittest():
import unittest

#import modulu (obiekt testowy()
import program

class TestProgram(unittest.TestCase):
    def test_zwroc_100(self):
        wynik = program.zwroc_100()
        self.assertEqual(wynik, 100)

    def test_zwroc_500(self):
        wynik = program.zwroc_500(400)
        self.assertEqual(wynik, 500)

if __name__ == '__main__':
    unittest.main()
