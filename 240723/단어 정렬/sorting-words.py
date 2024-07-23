n = int(input())

words = []

for _ in range(n):
    word = input()
    words.append(word)

words.sort()

for word in words:
    print(word)