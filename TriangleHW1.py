# -*- coding: utf-8 -*-
"""
1. Assignment Description: 
Your assignment is to write a program in Python to classify triangles and use an automated test platform,
e.g. UnitTest or PyTest, and write test cases to test your implementation of classifying triangles.  
The goal is for you to gain experience using automated test tools and to think through the issues associated
with testing a "system".  

2. Author: Sachin MC Reddy

"""
import unittest
import math 

def classifyTriangle(a,b,c):
    if a + b > c and a + c > b and b + c > a and min(a,b,c) > 0:
        if a == b == c :
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isoceles Triangle"
        else:
            if max(a,b,c) ** 2 == ((a + b + c) - max(a,b,c) - min(a,b,c)) ** 2 + min(a,b,c) ** 2:
                return "Right Triangle"
            else:
                return "Scalene Triangle"  
    else:
        return "Not A Triangle"

class TestTriangles(unittest.TestCase):
    
    ''' test function for equilateral triangle detection ''' 
    def test_Equilateral(self):
        self.assertEqual(classifyTriangle(4,4,4),"Equilateral Triangle")
        self.assertNotEqual(classifyTriangle(4,3,4),"Equilateral Triangle")  

    ''' test function for  isoceles triangle detection '''
    def test_Isoceles(self):
        self.assertEqual(classifyTriangle(3,4,4),"Isoceles Triangle")
        self.assertNotEqual(classifyTriangle(2,1,3),"Isoceles Triangle")
        
    ''' test rest triangle detection '''   
    def test_Right(self):
        self.assertEqual(classifyTriangle(3,4,5),"Right Triangle")
        self.assertNotEqual(classifyTriangle(6,10,6),"Right Triangle")
        
    ''' test scalene triangle detection '''
    def test_Scalene(self):
        self.assertEqual(classifyTriangle(3,4,6),"Scalene Triangle")
        self.assertNotEqual(classifyTriangle(3,4,5),"Scalene Triangle")
        
    ''' test function for not a triangle'''
    def test_Not_Triangle(self): 
        self.assertEqual(classifyTriangle(2,2,7),"Not A Triangle")
        self.assertEqual(classifyTriangle(4,0,8),"Not A Triangle")
        self.assertNotEqual (classifyTriangle(3,3,3),"Not A Triangle")
        
def resultClassifyTriangle(a,b,c):
    print('classifyTriangle(',a, ',', b, ',', c, ') = ' + classifyTriangle(a,b,c))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    resultClassifyTriangle(3,5,7)
    resultClassifyTriangle(2,0,4)
    resultClassifyTriangle(3,4,5)
    resultClassifyTriangle(4,5,4)
    resultClassifyTriangle(3,4,4)
    resultClassifyTriangle(6,4,5)
    resultClassifyTriangle(1,1,1)
   