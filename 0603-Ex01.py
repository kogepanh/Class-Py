#Ex01
colors = ["赤", "青", "黃", "緑", "紫"]

#先頭と後ろから2番めの色を表示
print("先頭は", colors[0])
print("後から2番目は", colors[len(colors)-2])

#順番に表示(Ver.1)
for i in range(len(colors)):
    print(i+1, "番目の色は", colors[i], "です")

#順番に表示(Ver.2)
i = 1;
for color in colors:
    print(i, "番目の色は", color, "です")
    i+=1;
