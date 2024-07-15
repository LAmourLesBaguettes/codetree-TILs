x = input()
arr = x.split()
a = int(arr[0])
b = int(arr[1])

if a > 0:
    for _ in range(b):
        print(a, end="") 
else:
    print("0")