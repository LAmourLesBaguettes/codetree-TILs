n = int(input())
elements= list(map(int, input().split()))

asc_sorted = sorted(elements)
print(" ".join(map(str, asc_sorted)))

desc_sorted = sorted(elements, reverse = True)
print(" ".join(map(str, desc_sorted)))