#06
import math

n = input("数を入力してください:")
n = int(n)
a = math.floor(math.sqrt(n/2))

for i in range(a):
    b = n - pow(i+1, 2)
    c = math.floor(math.sqrt(b))
    if(b == pow(c, 2)):
        print(i+1, ",", c)
