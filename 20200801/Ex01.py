#01
import random

sum_correct = 0

for i in range(10):
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    answer = int(input(f'{num1} + {num2} = ? '))
    if answer == num1+num2:
        print("正解です")
        sum_correct += 1
    else:
        print("不正解です")

if sum_correct == 10:
    tmp = "よくできました。"
elif sum_correct == 9:
    tmp = "惜しい!"
elif sum_correct >= 5:
    tmp = "もっと落ち着いて。"
else:
    tmp = "次回はもっと頑張りましょう。"

print(f'10問中{sum_correct}問正解でした。{tmp}')
