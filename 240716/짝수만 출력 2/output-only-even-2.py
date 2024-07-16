# Reading input
input_str = input("입력: ")
b, a = map(int, input_str.split())

# Ensure b is greater than a
if a > b:
    a, b = b, a

# Initialize the list of even numbers
even_numbers = []

# Using while loop to find even numbers in descending order
current = b
while current >= a:
    if current % 2 == 0:
        even_numbers.append(current)
    current -= 1

# Printing the result
print("출력: ", " ".join(map(str, even_numbers)))