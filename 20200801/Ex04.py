#04

sum_name = 0
sum_score = 0
max_score = 0
max_name =''
min_score = 100
min_name =''

f = open('data_a.txt', "r", encoding = "utf_8")
while True:
    line = f.readline()
    if line:
        l = line.split(',')

        sum_name += 1

        l[1] = int(l[1])
        sum_score += l[1]

        if l[1] >= max_score:
            max_name = l[0]
            max_score = l[1]

        if l[1] <= min_score:
            min_name = l[0]
            min_score = l[1]
    else:
        break

ave = round((sum_score/sum_name), 1)
print('平均点:', ave)
print('最高得点:', max_name, max_score, '点')
print('最低得点:', min_name, min_score, '点')
