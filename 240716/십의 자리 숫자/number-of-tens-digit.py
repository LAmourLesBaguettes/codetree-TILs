def count_tens_place(numbers):
    counts = [0] * 10
    for number in numbers:
        if number == 0:
            continue
        tens_place = number // 10
        if tens_place > 0:
            counts[tens_place] += 1
    return counts[1:]

numbers = list(map(int, input().split()))

result = count_tens_place(numbers)

for i in range(1, 10):
    print(f"{i} - {result[i-1]}")