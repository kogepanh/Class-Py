#ex03

# リストを逆順にする関数
def rev(lst):
   if lst == []:
          return []
   else:
          return rev(lst[1:]) + [lst[0]]

def deeprev(lst):
   if lst == []:
       return []
   else:
       return deeprev(lst[1:]) + [lst[0]]


# main
lst = [0, 1, 2]
print(f"rev({lst}) = {rev(lst)}")
lst1 = [[0, 1], [2, 3], [4, 5]]
print(f"deeprev({lst1}) = {deeprev(lst1)}")