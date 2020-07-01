# ex06
f = open("data.txt", mode="a", encoding="utf-8")

while True:
   word = input("費目を入力してください: ")
   if word == "END":
       break
   amount = input("金額を入力してください: ")
   s = word + '\t'
   s = s + amount
   f.write(s)
f.close()
