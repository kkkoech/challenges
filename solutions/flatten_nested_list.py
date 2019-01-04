'''
Given the array below, write a function to sum all the numeric elements, including sub-arrays. The solution should work for arbitrary depth of sub-arrays.

var arr = ['a', 1, 2, [3, 'b', 4, [5, 6, 'c']], 'd', 7, [8, 9]]
'''
nestedList = ['a', 1, 2, [3, 'b', 4, [5, 6, 'c']], 'd', 7, [8, 9]]

#Regex solution
import re 
def flattenList(elem):
    #convert nested list to a string:
    stringList = "%s"%(nestedList)
    
    #Using Regex to search for ints in the resulting string
    stringList = re.sub(r'\D', "", stringList)
    
    flattenedList = []
    for i in stringList:
        flattenedList.append(int(i))
    return flattenedList

print("-------- Regex Solution ------------")
print(flattenList(nestedList))

#Recursive approach
def flattenListRecursive(elem):
    flattenedList = []
    for i in elem:
        if isinstance(i, int):
            flattenedList.append(i)
        elif isinstance(i, list):
            flattenedList += flattenListRecursive(i)
    return flattenedList

print("-------- Recursive Solution --------")
print(flattenListRecursive(nestedList))


#Recursive solution 2

