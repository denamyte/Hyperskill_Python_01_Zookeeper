days = int(input())
food_per_day = int(input())
flight = int(input())
night_cost = int(input())
print(food_per_day * days
      + flight * 2
      + night_cost * (days - 1))
