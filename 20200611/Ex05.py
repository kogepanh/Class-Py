#05

sum_correct = 0     #正解数

question1 = ("四万十川が流れるのはどこか？")
print(question1)
choice1 = ["1.高知", "2.島根", "3.香川"]
i = 0
for i in range(len(choice1)):
    print(choice1[i], end="")
i += 1
answer1 = input("\n解答番号を入力してください: ")
if answer1 == "1":
    sum_correct += 1
    print("正解です")
else:
    print("残念，不正解です")


question2 = ("発酵食品ではないものはどれか？")
print(question2)
choice2 = ["1.メンマ", "2.鰹節", "3.梅干し"]
i = 0
for i in range(len(choice2)):
    print(choice2[i], end="")
i += 1
answer2 = input("\n解答番号を入力してください: ")
if answer2 == "3":
    sum_correct += 1
    print("正解です")
else:
    print("残念，不正解です")


question3 = ("ビタミンEを最も多く含むナッツはどれか？")
print(question3)
choice3 = ["1.カシューナッツ", "2.ピーナッツ", "3.アーモンド"]
i = 0
for i in range(len(choice3)):
    print(choice3[i], end="")
i += 1
answer3 = input("\n解答番号を入力してください: ")
if answer3 == "3":
    sum_correct += 1
    print("正解です")
else:
    print("残念，不正解です")

sum_per = round(sum_correct/3*100, 1)
print("正答率は", sum_per, "%です")    #正解数を問題数で除算
