import unittest
from parser import parse_checker

class ParserTests(unittest.TestCase):
    """
    A class to test the parse module
    """
    
    def testParser1(self):
        expression = "(2x+1)"
        self.assertTrue(parse_checker(expression), "L'expression (2x+1) devrait être bonne")
        
    def testParser2(self):
        expression = "(2x+1))"
        self.assertFalse(parse_checker(expression), "L'expression (2x+1)) devrait être fausse")
        
    def testParser3(self):
        expression = ")1x()"
        self.assertFalse(parse_checker(expression), "L'expression )1x() devrait être fausse")
        
    def testParser4(self):
        expression = "[(2x+1)]"
        self.assertTrue(parse_checker(expression), "L'expression [(2x+1)] devrait être bonne")
        
    def testParser5(self):
        expression = "[(2x+1])"
        self.assertFalse(parse_checker(expression), "L'expression [(2x+1]) devrait être fausse")
        
if __name__ == '__main__':
    unittest.main()            