# ex03

class Polygon:
    def __init__(self, amount, length):
        self.amount = amount
        self.length = length
    
    def perimeter(self):
        return self.amount * self.length

    def __str__(self):
        return f"[Polygon] 辺の数: {self.amount}, 辺の長さ: {self.length:d}"

class Triangle(Polygon):
    def __init__(self, length):
        super().__init__(3, length)

    def area(self):
        import math
        return math.sqrt(3) * self.length * self.length / 4

class Square(Polygon):
    def __init__(self, length):
        super().__init__(4, length)

    def area(self):
        import math
        return self.length * self.length

# main
triangle1 = Triangle(10)
print(triangle1)
print("周囲の長さ", triangle1.perimeter())
print("面積:", triangle1.area())

square1 = Square(20)
print(square1)
print("周囲の長さ", square1.perimeter())
print("面積：", square1.area())
