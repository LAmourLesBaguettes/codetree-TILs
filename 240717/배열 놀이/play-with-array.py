# Read input values
n, q = map(int, input().strip().split())
elements = list(map(int, input().strip().split()))

# Process each query
queries = [input().strip().split() for _ in range(q)]

for query in queries:
    if query[0] == "1":
        # "1 a": Output the a-th element
        a = int(query[1])
        print(elements[a - 1])
    
    elif query[0] == "2":
        # "2 b": Find the index of the element with value b
        b = int(query[1])
        if b in elements:
            print(elements.index(b) + 1)
        else:
            print(0)
    
    elif query[0] == "3":
        # "3 s e": Output the elements from s-th to e-th
        s, e = int(query[1]), int(query[2])
        print(" ".join(map(str, elements[s - 1:e])))