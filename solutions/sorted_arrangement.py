def binary_search(lst, item):
    start = 0
    end = len(lst)
    mid = start + (end-start)// 2
    #end = len(lst)
    if len(lst) == 1:
        if lst[0] == item:
            return 
    if lst[mid] == item: 
        return mid
    elif lst[mid] > item:
        end = mid-1
        return binary_search(lst[:end],  item)
    elif lst[mid] < item:
        start = mid
        return binary_search(lst[start:], item)
    else:
        return -1

print(binary_search([1,2,3,4],5))

