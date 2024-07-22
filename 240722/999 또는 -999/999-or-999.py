numbers = list(map(int, input().split()))

min_number = 1000
max_number = -1000

for number in numbers:
    if number == 999 or number == -999:
        break
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(max_number, min_number)