n = int(input())
numbers = list(map(int, input().split()))

current_numbers = []

results = []

for i in range(n):
    current_numbers.append(numbers[i])
    current_numbers.sort()


    if (i +1) % 2 ==1:
        median = current_numbers[i//2]
        results.append(median)

print(" ".join(map(str, results)))