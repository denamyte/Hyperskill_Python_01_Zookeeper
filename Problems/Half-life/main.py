current, final = int(input()), int(input())
half_lives = 0
while current >= final:
    current //= 2
    half_lives += 1
print(half_lives * 12)
