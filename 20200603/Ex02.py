#Ex02

dic = {}    #空のディクショナリを用意

while True: #無限に繰り返す
    key = input("キーを入力してください: ")
    if key == "END":    #入力されたのは "END" か？
        break
    val = input("値を入力してください: ")
    dic[key] = val  #ディクショナリ(dic)にキーと値の組を格納(追加)

#すべてのキーいついてキーと値の組を表示
for k,v in dic.items():
    print(k,v)
