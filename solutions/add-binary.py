'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
#idea: convert binary to decimal. Add. Them convert back to binary
def add_binary(a,b):
    #binary to decimal
    def to_decimal(c):
        decimal_val = 0
        for pos in range(len(c)):
            decimal_val += 2**(len(c)-(pos+1)) * int(c[pos])
        return decimal_val

    #decimal to binary
    def to_binary(c):
        if c == 0:
            return 0
        bins = ""
        while c > 0:    
            bins = str(c % 2) + bins
            c = c // 2
        return bins
    
    return to_binary(to_decimal(a) + to_decimal(b))

#tests
print(add_binary("0","0"))
print(add_binary("1","1"))
print(add_binary("111","100"))

# solution II
def addBinary(a, b):
    list1 = list(a)
    list2 = list(b)
    x = -1
    ans = []
    quot = 0
    
    for i in range(max([len(list1), len(list2)])):
        try:
            ans = [str((int(list1[x]) + int(list2[x]) + quot) % 2)] + ans
            quot = (int(list1[x]) + int(list2[x]) + quot) // 2
        except:
            try:
                ans = [str((int(list1[x]) + quot) % 2)] + ans
                quot = (int(list1[x]) + quot) // 2
            except:
                ans = [str((int(list2[x]) + quot) % 2)] + ans
                quot = (int(list2[x]) + quot) // 2
        x -= 1
    ans = [str(quot)] + ans
    return ''.join(ans)

print(addBinary('1111', '111'))
