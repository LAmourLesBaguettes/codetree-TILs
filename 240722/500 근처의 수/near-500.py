numbers = map(int, input().split())

max_below_500 = -1

min_below500 = 1001

for number in numbers:
    if number < 500 and number > max_below_500:
        max_below_500 = number
    elif number > 500 and number< min_below500:
        min_below500 = number

print(max_below_500, min_below500)