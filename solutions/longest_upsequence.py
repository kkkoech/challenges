
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


#Solution 2, also very recursive:

def first(xs):
    # returns first upsequence of a list
    if len(xs)==0:
        return 0
    elif len(xs)==1:
        return 1
    else:
        if xs[0]<xs[1]:
            return 1+first(xs[1:])
        else:
            return 1

print(first([1,0,12,3,2]))



#returns longest upsequence of a list
def longest(xs):
    if len(xs)==0:
        return 0
    elif len(xs)==1:
        return 1
    else:
        pos = first(xs)
        # if pos<len(xs):
        return max(pos, longest(xs[pos:]))
        # else:
        #     return pos


print("LONGEST TEST")
print( longest([3,4,5,6,3,4,6,1,2]) )
print( longest([1,2,0,1,0,1,2,6,0,1,1])) #4
print( longest([1,2,3,4,5])) #5
print( longest([1,2,5,8,0,1,0,1,0])) #4
print( longest([1,2,0,1,3,4,0,3,2])) #4
print( longest([9,7,6,5,4])) #1
print( longest([9,7,6,5,4,0,1])) #2
print( longest([0,1,2,3,4,0,0])) #5
print( longest([0,1,2,3,4,2,1])) #5
print(longest([1,3,1,2,3])) #3
print(longest([1,3,2,1,2,3])) #3

print(longest([2]))
print(longest([3,1]))
print(longest([3,1,2]))


