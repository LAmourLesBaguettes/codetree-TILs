N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

max_sum = 0

for i in range(N):
    group_sum = numbers[i] + numbers[2*N - 1 - i]
    max_sum = max(max_sum, group_sum)


print(max_sum)