N = int(input())
unique_words = set()

for _ in range(N):
    word = input().strip()
    rotations = set()

    for i in range(len(word)):
        rotated_word = word[i:] + word[:i]
        rotations.add(rotated_word)
    
    if not unique_words.intersection(rotations):
        unique_words.add(word)

print(len(unique_words))
