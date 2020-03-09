#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:27:48 2020

@author: sachinmcreddy
"""
from hw5 import triangle
import unittest
class TestCases(unittest.TestCase):


    def test_equilateral_triangle(self):
        assert triangle(2, 2, 2) == 'Equilateral triangle'
        
    def test_right_angled_triangle(self):
        assert triangle(16, 18, 9) == 'Right angled triangle'

    def test_isoceles_triangle(self):
        assert triangle(15, 15, 11) != 'Isoceles triangle'

    def test_Scalene_triangle(self):
        assert triangle(12, 8, 13) == 'Scalene triangle'

    def test_invalid_triangle(self):
        assert triangle(-8, 100, -0) == 'invalid input'