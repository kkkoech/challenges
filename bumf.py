def add_binary(a,b):
    
    def add(c,d):
        if c==d=="1":
            return "10"
        return str(int(c) or int(d) )

    if len(a)>len(b):
        diff = len(a)-len(b)
        b = (diff*"0") + b 
    elif len(b)>len(a):
        diff = len(b)-len(a)
        a = (diff*"0") + a 
    list_a = list(a)
    list_b = list(b)

    
    bin_str = []
    for i in range(len(list_a)):
        term = add(list_a[len(list_a)-1-i], list_b[len(list_a)-1-i])
        bin_str.append(term)
    for j in range(len(bin_str)):
        if len(bin_str[len(bin_str)-1-j])>1:
            bin_str[len(bin_str)-1-j] =( bin_str[len(bin_str)-1-j])[-1]
            bin_str[len(bin_str)-2-j] = add(bin_str[len(bin_str)-2-j], "1")
    '''
    for j in (len(bins)-1) - range(1,len(bins)):
        if bins[j] == "10":
            bins[j] = "0"
            bins[j-1] = add(bins[j-1], "1")
    
    bin_string = ""
    for k in bins:
        bin_string += k 
    
    bin_int = 0
    for k in range(len(bins)):
        bin_int += int(bins[k])*10**(len(bins)-1)
    '''    
    return bin_str

print(add_binary("11", "11"))