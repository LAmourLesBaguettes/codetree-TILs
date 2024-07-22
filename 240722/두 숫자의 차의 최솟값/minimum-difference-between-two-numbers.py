N = int(input())

numbers = list(map(int, input().split()))

min_diff = float('inf')

for i in range(n-1):
    diff = numbers[i-1] - numbers[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)