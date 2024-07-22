N = int(input())

numbers = map(int(input().split()))

count_dict = {}

for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

unique_numbers = [number for number in count_dict if count_dict[number] == 1]

if unique_numbers:
    max_unique_number = max(unique_numbers)
else:
    max_unique_number = -1

print(max_unique_number)