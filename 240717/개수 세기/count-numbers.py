# Read the input values
n, m = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

# Count the occurrences of m in the numbers list
count_m = numbers.count(m)

# Output the result
print(count_m)