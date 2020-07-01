#Ex03

#リストを定義
hanwa = ["天王寺", "美章園", "南田辺", "鶴ケ丘", "長居", "我孫子町", "杉本町"]

#入力
s = input("どこから? ")
d = input("どこまで? ")
start = int(s)
dest = int(d) + 1

if start > dest or start < 0 or dest > 6:   #範囲外の場合
    print("正しく入力してください")
else:   #正しい入力範囲の場合
    route = hanwa[start:dest]   #リストをスライス
    for station in route:
        print(start, station)
        start += 1