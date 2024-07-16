def print_multiples(n):
    count_five_multiples = 0
    multiple = 1
    result = []


    while count_five_multiples < 2:
        value = n * multiple
        result.append(value)
        if value % 5 == 0:
            count_five_multiples += 1
        multiple += 1

    print(" ".join(map(str, result)))

n = int(input())
print_multiples(n)