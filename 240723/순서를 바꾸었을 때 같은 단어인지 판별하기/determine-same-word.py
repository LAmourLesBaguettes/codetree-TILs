from collections import Counter

word1 = input().strip()
word2 = input().strip()

counter1 = Counter(word1)
counter2 = Counter(word2)

if counter1 == counter2:
    print("Yes")
else:
    print("No")