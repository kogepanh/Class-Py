# ex03
n = int(input("正の整数を入力してください:　"))

tmp = 0
for i in range(2, n):
    if n % i == 0:
        tmp = 1

if tmp == 1:
    print(n, "は素数ではありません")
else:
    print(n, "は素数です")
   