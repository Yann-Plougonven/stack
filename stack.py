#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stack:
    """An implementation of a Stack"""
    
    def __init__(self):
        self._elements=[]
    
    def isEmpty(self):
        """
        Return True if the stack is empty, False otherwise
        """
        if self._elements == []:
            return True
        elif self._elements != []:
            return False
    
    def push(self, element):
        """
        Push an element into the stack
        return the stack
        """
        self._elements.append(element)
        return self  # On return la pile elle même, pas la liste

    def pop(self):
        """
        pop an element from the stack
        return the poped element
        """
        return self._elements.pop()

    def summit(self):
        """
        read the top element of the stack without removing it.
        return the top element.
        """
        return self._elements[-1]

    def size(self):
        """
        read the size of the stack
        return the size as an integer.
        """
        return len(self._elements)
    
    def __len__(self):
        return self.size()
        
        