"""
    Write a python program to print all positive numbers in a range.

    EXAMPLE
    Input: list = [12, -7, 5, 64, -14]
    Output: [12, 5, 64]
"""

list = []
n = int (input ('Enter the number of elements in the list: '))

print ("Enter the elements of the List: ")
i = 0
while i<n:
    x = int (input())
    list.append (x)
    i += 1

print ("Positive number in the List are: ", end = " ")
for j in list:
    if j>=0:
        print (j, end = " ")