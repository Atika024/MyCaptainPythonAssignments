"""
    Write a python program for fibonacci numbers.
    0, 1, 1, 2, 3, 5, 8, 13, ...    
"""

n = int (input ('Enter the number of digits in the Fibonacci series: '))
first = 0
second = 1
i = 2

print (first)
print (second)
while i<n:
    third = first+second
    first = second
    second = third
    print (third)
    i += 1