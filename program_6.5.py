"""
Created on January  25, 2020
by Kush Paliwal

Think Python 2e Exercise 5.2
This program finds the (greatest commom divisor) gcd of two given numbers
"""
# Define gcd function
def gcd(a,b):
    if b == 0:
        print(a)
    else:
        r = a%b
        return gcd(b,r)

# Take input from user    
a = input('Input a: ')
b = input('Input b: ')

# Convert str to float
a = float(a)
b = float(b)

# Call function
gcd(a,b)
