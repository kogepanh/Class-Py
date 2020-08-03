#02

n = int(input("数を入力してください:"))

a = ' '
b = '*'

for i in range(n+1):
    tmp = ''
    for j in range(n-i):
        tmp += a
    for k in range(i):
        tmp = tmp + b + b
    print(tmp + b)

for i in reversed(range(n)):
    tmp = ''
    for j in range(n-i):
        tmp += a
    for k in range(i):
        tmp = tmp + b + b
    print(tmp + b)
