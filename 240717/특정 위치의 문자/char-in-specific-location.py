# Initialize the array
char_array = ['L', 'E', 'B', 'R', 'O', 'S']

# Input character
input_char = input().strip()

# Find the index of the input character in the array
if input_char in char_array:
    result = char_array.index(input_char)
else:
    result = "None"

# Output the result
print(result)