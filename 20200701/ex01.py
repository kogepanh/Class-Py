# ex01

# 「本」のクラス
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"「{self.title} by {self.author}」"


# main
book1 = Book("吾輩は猫である", "夏目漱石")
book2 = Book("銀河鉄道", "宮沢賢治")

print(book1)
print(book2)
print(book1.title)
print(book2.author)
