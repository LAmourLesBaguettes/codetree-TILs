# Input: Read an integer from the input
n = int(input())

# Edge case: If the number is 0, its binary representation is also 0
if n == 0:
    print(0)
else:
    binary_representation = ""
    while n > 0:
        remainder = n % 2
        binary_representation = str(remainder) + binary_representation
        n = n // 2

    print(binary_representation)