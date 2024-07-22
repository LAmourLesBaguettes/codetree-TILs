N = int(input())

numbers = list(map(int, input().split()))

min_number = min(numbers)

min_count = numbers.count(min_number)

print(min_number, min_count)