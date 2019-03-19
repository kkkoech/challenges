
#This is a recursive solution 
#Solution 1





#Solution 2
#returns index of list where it starts to decrease
def decrease_index(l):
    if l == []:
        return 0
    elif len(l)==1:
        return 0
    elif l[1] > l[0]:
        return 1 + decrease_index(l[1:])
    else:
        return 0
print(decrease_index([1,2,3,0])) #returns 2

def longest_sequence(l):
    if l == []:
        return 0 
    elif len(l) ==1:
        return 1
    else: 
        return max(decrease_index(l[0:3]),decrease_index(l[2:])) + 1 
        #Because length of the longest upsequence would be decrease_index() + 1


print(longest_sequence([4,1,5,2,6,3,2])) #returns 1
print(longest_sequence([1,2,3])) #returns 3 
print(longest_sequence([1,2,3,0])) #returns 3
print(longest_sequence([4,3,2,1])) #returns 1
print(longest_sequence([1])) #returns 1
print(longest_sequence([])) #returns 0 

