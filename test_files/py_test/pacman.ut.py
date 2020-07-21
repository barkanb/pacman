"""
Unit tests for pacman.py
Last Modified: April 29, 2019
"""

import os
import sys
import time
import unittest
from pacman import pacman

class AllTests(unittest.TestCase):
    def test_runtime(self):
        self.assertEqual(pacman("runtime.txt"), (2142, 147, 148))

    def test_input(self):
        self.assertEqual(pacman("input.txt"), (1, 4, 7))

    def test_input2(self):
        self.assertEqual(pacman("input2.txt"), (10, 84, 20))

    def test_generic(self):
        self.assertEqual(pacman("generic.txt"), (6, 1, 27))

    def test_edge(self):
        self.assertEqual(pacman("edge.txt"), (-1, -1, 0))

    def test_err1(self):
        self.assertEqual(pacman("err1.txt"), (-1, -1, 0))

    def test_err2(self):
        self.assertEqual(pacman("err2.txt"), (-1, -1, 0))

    def test_err3(self):
        self.assertEqual(pacman("err3.txt"), (-1, -1, 0))

    def test_err4(self):
        self.assertEqual(pacman("err4.txt"), (-1, -1, 0))

    def test_err5(self):
        self.assertEqual(pacman("err5.txt"), (-1, -1, 0))


if __name__ == '__main__':
    for testClass in [AllTests]:
        print('\n\nTest Class: {}\n'.format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
