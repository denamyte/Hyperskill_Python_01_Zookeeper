money = int(input())
limit, percent, years = 700000, 1.071, 0
while money <= limit:
    years += 1
    money *= percent
    # print(money)
print(years)
