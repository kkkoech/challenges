'''
def ideals(l,r):
    num_range = [i for i in range(l,r+1)]
    for number in range(l,r+1):
'''



def ideals(l,r):
    def recursive_divide(n):
        if n == 0:
            return 0
        elif (n % 5) == 0:
            quot = n / 5
            return recursive_divide(quot)
        elif (n % 3) == 0:
            quot = n / 3
            return recursive_divide(quot)
        else:
            return int(n)
    num_range = [i for i in range(l,r+1) if i != 1]
    #ideals = list(map(lambda x: x if recursive_divide(x)==1 else None, num_range))
    
    ideals = []
    for num in num_range:
        if recursive_divide(num) == 1:
            ideals.append(num)
    return len(ideals)

print(ideals(1,1))


    



