num = int(input())
sum_ = num % 10
num //= 10
sum_ += num % 10
sum_ += num // 10
print(sum_)
