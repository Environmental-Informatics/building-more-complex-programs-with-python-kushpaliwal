"""
Created on January  25, 2020
by Kush Paliwal

Think Python 2e Exercise 5.2
This program checks Fermat's theorem
"""

# Define function to check Fermats theorem
def check_fermat(a,b,c,n):
    if  n>2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')
        
# Take input from user and call check_fermat function
def ferm_input():
    a = input('Input a\n')
    b = input('Input b\n')
    c = input('Input c\n')
    n = input('Input n\n')
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    check_fermat(a,b,c,n)
    
# Call function
ferm_input()