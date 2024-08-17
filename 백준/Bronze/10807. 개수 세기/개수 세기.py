import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
V = int(input())
cnt = 0
for n in numbers:
    if n == V:
        cnt += 1

print(cnt)