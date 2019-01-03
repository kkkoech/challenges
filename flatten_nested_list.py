'''
Given the array below, write a function to sum all the numeric elements, including sub-arrays. The solution should work for arbitrary depth of sub-arrays.

var arr = ['a', 1, 2, [3, 'b', 4, [5, 6, 'c']], 'd', 7, [8, 9]]
'''
nestedList = ['a', 1, 2, [3, 'b', 4, [5, 6, 'c']], 'd', 7, [8, 9]]

#Regex solution
import re 
def sumElements(elem):
    #convert nested list to a string:
    stringList = "%s"%(nestedList)
    
    #Using Regex to search for ints in the resulting string
    stringList = re.sub(r'\D', "", stringList)
    
    sumElems = 0
    for i in stringList:
        sumElems += int(i)
    return sumElems 

print("--------SumElements with Regex-----------")
print(sumElements(nestedList))

#Recursive approach
def sumElementsRecursive(elem):
    sumElems = 0
    i = 0
    for i in elem:
        if isinstance(i, int):
            sumElems += i
        elif isinstance(i, list):
            sumElems += sumElementsRecursive(i)
    return sumElems

print("--------SumElements with Recursion--------")
print(sumElementsRecursive(nestedList))
