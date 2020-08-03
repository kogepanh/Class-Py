#08

def re_factorial(n):
    if n < 2:
        return 1
    return n * re_factorial(n-1)

fact = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    fact[i] = re_factorial(i)

total = []
for i in range(9999999):
    n = list(str(i))
    tmp = 0
    for j in range(len(n)):
        tmp += fact[int(n[j])]

    if tmp == i:
        total.append(i)

print(total)
