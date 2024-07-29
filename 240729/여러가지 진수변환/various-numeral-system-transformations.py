# Input: Read the integer N and the base B
N, B = map(int, input().split())

# Edge case: If N is 0, its representation in any base is also 0
if N == 0:
    print(0)
else:
    base_representation = ""
    while N > 0:
        remainder = N % B
        base_representation = str(remainder) + base_representation
        N = N // B

    print(base_representation)