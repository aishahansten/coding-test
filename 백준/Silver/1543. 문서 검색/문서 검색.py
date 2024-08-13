import sys
input = sys.stdin.readline

word = input().strip()
target = input().strip()

cnt = 0
i = 0

while i < len(word):
    if word[i:i+len(target)] == target:
        cnt += 1
        i += len(target)
    else:
        i += 1
print(cnt)