"""
Task 1: Write a Python program which accepts the radius of a circle from the user and computes area.
"""

PI = 3.14
r = float (input("Input the radius of the circle: "))
area = PI*r*r
print ("The area of the circle with radius ", r, " is: ", area)


"""
Task 2: Write a Python program to accept a filename from the user and print the extension of that.
"""

myDict = {
    "abc.py":"Python",
    "abc.c":"C",
    "abc.cpp":"C++",
    "abc.html":"HTML",
    "abc.js":"Javascript",
    "abc.java":"Java",
    "abc.css":"CSS"
}

ext = input ("Enter the filename: abc.")
print ("The extension of the file is: ", myDict["abc."+ext])