#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from stack import Stack

class StackTests(unittest.TestCase):
    """
    A class to test the Stack module
    """
    def setUp(self):
        """
        create an empty Stack for all tests
        """
        self.stack=Stack()

    def testPush(self):
        """
        Check if the push method works
        """
        element='element'
        mystack=self.stack.push(element)
        self.assertTrue(isinstance(mystack, Stack), "The push method should return an instance of Stack")
        
        
    def testPop(self):
        """
        check if the pop method works
        """
        elements=['How','are','you','today','?']
        
        for e in elements:
            self.stack.push(e)
        pops=[self.stack.pop() for e in elements]
        reverse=elements[::-1] #we reverse the input list
        self.assertEqual(reverse, pops, "pops elements should be %s, but we have %s instead."%(reverse, pops))
        with self.assertRaises(IndexError):
            self.stack.pop()

    def testIsEmpty(self):
        """
        Check if the isEmpty method works
        """
        answer1=self.stack.isEmpty()
        self.assertEqual(answer1, True, "isEmpty should be True, it returned %s instead."%answer1)
        element='element'
        self.stack.push(element)
        answer2=self.stack.isEmpty()
        self.assertEqual(answer2, False, "isEmpty should be False, it returned %s instead."%answer2)
        
    def testSize(self):
        """
        Check if the size method works
        """
        size1=self.stack.size()
        self.assertEqual(size1, 0, "size should be 0, it returned %s instead."%size1)
        self.stack.push('test')
        size2=self.stack.size()
        self.assertEqual(size2, 1, "size should be 1, it returned %s instead."%size2)
        self.stack.pop()
        size3=self.stack.size()
        self.assertEqual(size3, 0, "size should be 0, it returned %s instead."%size3)
        
    def testSummit(self):
        """
        Check if the summit method works
        """
        elements=['How','are','you','today','?']
        
        for e in elements:
            self.stack.push(e)
        summit1=self.stack.summit()
        self.assertEqual(elements[-1], summit1, "summit should be %s, it returned %s instead."%(elements[-1], summit1))
        self.stack.pop()
        summit2=self.stack.summit()
        self.assertEqual(elements[-2], summit2, "summit should be %s, it returned %s instead."%(elements[-2], summit2))
        self.stack=Stack()
        with self.assertRaises(IndexError):
            self.stack.summit()
            
    def test__len__(self):
        """
        Check if len method works
        """
        maPile = self.stack
        self.assertEqual(len(maPile), 0, "La pile devrait être égale à 0, mais c'est pas le cas")
        maPile.push("coucou")
        self.assertEqual(len(maPile), 1, "La pile devrait être égale à 1, mais c'est pas le cas")
        
    def testAaa(self):
        """
        Test if
        """
        
        
if __name__ == '__main__':
    unittest.main()        