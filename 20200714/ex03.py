#ex03
def rev(lst):
    if lst == []:
        return []
    else:
        return rev(lst[1:]) + [lst[0]]

def deeprev(lst):
    if lst == []:
        return []
    if isinstance(lst[0], list):
        lst[0] = deeprev(lst[0])
    return deeprev(lst[1:]) + [lst[0]]

def count_items(itemlist):
    if len(itemlist) == 0:
        return 0
    if not isinstance(itemlist, list):
        return 1
    return len(itemlist[0]) + count_items(itemlist[1:])

# main
lst1 = [0, 1, 2]
print 'deeprev(', lst1, ') =', deeprev(lst1)

lst2 = [[0, 1], [2, 3], [4, 5]]
print 'deeprev(', lst2, ') =', deeprev(lst2)

lst3 = [[[0, 1], [2, 3]], 4, [5, 6]]
print 'deeprev(', lst3, ') =', deeprev(lst3)

lst4 = [0, 1, [2, [3, 4]]]
print 'deeprev(', lst4, ') =', deeprev(lst4)
