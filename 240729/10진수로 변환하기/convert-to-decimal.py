# Input: Read the binary number as a string
binary_number = input().strip()

# Convert binary to decimal
decimal_number = 0
length = len(binary_number)
for i in range(length):
    # Calculate the value of the current bit
    bit_value = int(binary_number[length - 1 - i])
    decimal_number += bit_value * (2 ** i)

# Output the result
print(decimal_number)