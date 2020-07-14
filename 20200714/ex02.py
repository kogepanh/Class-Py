# ex02

def count_items(itemlist):
    if len(itemlist) == 0:
        return 0
    if not isinstance(itemlist, list):
        return 1
    return count_items(itemlist[0]) + count_items(itemlist[1:])

lst1 = ["a", "b", "c"]
print 'count_items(', lst1, ') =', count_items(lst1)

lst2 = ["a", ["b", "c"], "d"]
print 'count_items(', lst2, ') =', count_items(lst2)

lst3 = ["a", ["b", ["c", "d", "e"], ["f", "g"]]]
print 'count_items(', lst3, ') =', count_items(lst3)

str1 = "abc"
print 'count_items(', str1, ') =', count_items(str1)
