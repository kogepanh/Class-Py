# ex04
import random

def weather():
    k = random.randint(0, 99)
    if k < 45:
        return "晴れ"
    if 45 <= k < 75:
        return "曇り"
    if 75 <= k < 95:
        return "雨"
    if 95 <= k < 100:
        return "雪"
        
n = 10
while(0 < n):
    print(weather())
    n -= 1
