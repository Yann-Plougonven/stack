import unittest
from parser import parse_checker

class ParserTests(unittest.TestCase):
    """
    A class to test the parse module
    """
    def testParserTrue(self):
        expressions_vraies = ("(2x+1)", "[(2x+1)]", "([25])", "[(2*3)+2(2n+1)]", "")  # Liste des expressions vraies à tester
        for expression in expressions_vraies:
            self.assertTrue(parse_checker(expression), f"L'expression {expression} devrait être bonne")
        
    def testParserFalse(self):
        expressions_fausses = ("(2x+1))", ")1x()", "[(2x+1])", "]2[", "(2]", "][", ")[", "[)", ")(")  # Liste des expressions fausses à tester
        for expression in expressions_fausses:
            self.assertFalse(parse_checker(expression), f"L'expression {expression} devrait être fausse")
        
if __name__ == '__main__':
    unittest.main()            