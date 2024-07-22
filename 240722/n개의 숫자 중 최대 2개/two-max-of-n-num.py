N = int(input())

numbers = list(map(int, input().split()))

sorted_numbers = sorted(numbers, reverse = True)

print(sorted_numbers[0], sorted_numbers[1])