n = int(input())

words = []

for _ i in range(n):
    word = input()
    words.append(word)

words.sort()

for word in words:
    print(word)