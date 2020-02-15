"""
Created on January  25, 2020
by Kush Paliwal

Think Python 2e Exercise 5.2
This program finds the (greatest commom divisor) gcd of two given numbers
"""
# define gcd function
def gcd(a,b):
    if b == 0:
        return a
    else:
        r = a%b
        return gcd(b,r)
    
ans = gcd(10,6)
print(ans)