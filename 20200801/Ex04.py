#04

hg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(hg)

f = open('data_h.txt', "r", encoding = "utf_8")
while True:
    line = f.readline()
    if line:
        tmp = int(line)

        if tmp < 10:
            hg[0] += 1
        elif tmp < 20:
            hg[1] += 1
        elif tmp < 30:
            hg[2] += 1
        elif tmp < 40:
            hg[3] += 1
        elif tmp < 50:
            hg[4] += 1
        elif tmp < 60:
            hg[5] += 1
        elif tmp < 70:
            hg[6] += 1
        elif tmp < 80:
            hg[7] += 1
        elif tmp < 90:
            hg[8] += 1
        else:
            hg[9] += 1
    else:
        break

for i in range(len(hg)):
    tmp = ''
    for j in range(hg[i]):
        tmp += '*'
    print(i*10, "|", tmp)
