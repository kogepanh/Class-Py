# ex02

class Polygon:
    def __init__(self, amount, length):
        self.amount = amount
        self.length = length
    
    def perimeter(self):
        return self.amount * self.length

    def __str__(self):
        return f"[Polygon] 辺の数: {self.amount}, 辺の長さ: {self.length:d}"

polygon1 = Polygon(5, 100)
print(polygon1)
print(polygon1.amount)
print(polygon1.perimeter())
