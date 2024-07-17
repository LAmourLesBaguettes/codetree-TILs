# Read input values
n1, n2 = map(int, input().strip().split())
sequence_A = list(map(int, input().strip().split()))
sequence_B = list(map(int, input().strip().split()))

# Function to check if B is a contiguous subsequence of A
def is_contiguous_subsequence(A, B):
    n1, n2 = len(A), len(B)
    for i in range(n1 - n2 + 1):
        if A[i:i + n2] == B:
            return True
    return False

# Check if sequence B is a contiguous subsequence of sequence A
if is_contiguous_subsequence(sequence_A, sequence_B):
    print("Yes")
else:
    print("No")