# ex02

def count_items(itemlist):
   if itemlist == []:
       return []
   if not isinstance(itemlist, list):
       return len(itemlist)
   return len(itemlist[0]) + len(itemlist[1:])

lst1 = ["a", "b", "c"]
lst2 = ["a", ["b", "c"], "d"]
print(f"count_items{lst1} = {count_items(lst1)}")
print(f"count_items{lst2} = {count_items(lst2)}")