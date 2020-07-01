# ex04

class Counter:
    def __init__(self):
        self.count = 0

    def __str__(self):
        return f"現在のカウンタは {self.count} です。"

    def up(self):
        self.count += 1
        print("カウンタの値を1増やしました。現在のカウンタは" ,self.count, "です。")

    def down(self):
        self.count -= 1
        print("カウンタの値を1減らしました。現在のカウンタは" ,self.count, "です。")

# main
count1 = Counter()
count1.up()
count1.up()
print(count1)
count1.down()
print(count1)
