#Ex05

table = [[100, 50, 32, 25],
         [ 80, 45, 99, 12],
         [  3, 43, 18,  9]]

lst = []

for i in range(len(table[0])):  #各列をループ
    tmp = 0
    for j in range(len(table)): #各行をループ
        tmp += table[j][i]
    lst.append(tmp) #リストに追加

print("各列の合計値のリスト:", lst)