n ,k, T = input().split()
n = int(n)
k = int(k)

words = []
for _ in range(n):
    word = input().strip()
    words.append(word)

filtered_words = [word for word in words if word.startswith(T)]

filtered_words.sort()

print(filtered_words[k-1])