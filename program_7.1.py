"""
Created on January  25, 2020
by Kush Paliwal

Think Python 2e Exercise 5.2

test_square_root(a)
This program checks the square root of numbers from a to a+9
"""

# import library
import math

# define function to calculate the estimated square root
def mysqrt(a):
    x=a/2
    while True:
        epsilon = 0.000001
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y
        
# define function to print table
def test_square_root(a):
    b=a+10
    print('a\t','mysqrt(a)\t','math.sqrt(a)\t', 'diff')
    print('-\t ---------\t ------------\t ----')
    while a<b:
        diff = abs(math.sqrt(a) - mysqrt(a))
        print("{0:.1f}".format(a),"\t","{0:.10f}".format(mysqrt(a)),"\t","{0:.10f}".format(math.sqrt(a)),"\t",diff,'\n')
        a += 1
        
# call function
test_square_root(1)