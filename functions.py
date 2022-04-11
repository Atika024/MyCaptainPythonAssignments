"""
    Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
    
    Input : Please enter a string Mississippi
    Output : i = 04 s = 04 p =02 m =01
"""


def most_frequent (s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    return dict


str = input ("Enter a string: ")

myDict = most_frequent (str)
for w in sorted(myDict, key = myDict.get, reverse = True):
    print(w, " = ", myDict[w])