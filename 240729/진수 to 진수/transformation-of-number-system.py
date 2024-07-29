# Input: Read bases a and b, and the number n in base a
a, b = map(int, input().split())
n = input().strip()

# Step 1: Convert the number n from base a to decimal (base 10)
decimal_number = int(n, a)

# Step 2: Convert the decimal number to base b
# We use a loop to determine the digits in the base b representation
if decimal_number == 0:
    # If the number is zero, its representation in any base is also zero
    print(0)
else:
    b_base_representation = ""
    while decimal_number > 0:
        remainder = decimal_number % b
        b_base_representation = str(remainder) + b_base_representation
        decimal_number //= b

    # Output the result in base b
    print(b_base_representation)