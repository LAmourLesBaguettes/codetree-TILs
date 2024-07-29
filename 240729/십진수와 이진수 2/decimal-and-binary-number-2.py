# Input: Read the binary number as a string
binary_input = input().strip()

# Convert the binary number to a decimal integer
decimal_number = int(binary_input, 2)

# Multiply the decimal number by 17
multiplied_number = decimal_number * 17

# Convert the result back to a binary string
# The [2:] part removes the '0b' prefix that Python includes in the binary representation
binary_output = bin(multiplied_number)[2:]

# Output the binary result
print(binary_output)