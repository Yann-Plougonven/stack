import unittest
from calculeur import resultat

class CalculeurTests(unittest.TestCase):
    """
    A class to test the calculeur module
    """
    def test1(self):
        expressions = [('3', '4', '*', '2', '+'), ('2', '4', '+', '6', '-', '1', '+'), ('1', '19', '+', '2', '-'), ('0', '2', '-', '2', '+', '10', '-'), ('2', '3', '4', '+', '*')]
        results = (14, 1, 18, -10, 14)
        for i in range(len(expressions)):
            self.assertEqual(resultat(expressions[i]), results[i], f"L'expression {expressions[i]} devrait être égale à {results[i]}")

if __name__ == '__main__':
    unittest.main()