import sys

input = sys.stdin.readline

N = int(input())
seats = input().strip()

if 'L' in seats:
    cnt = 1
elif 'L' not in seats:
    cnt = 0
for s in seats:
    if s == 'S':
        cnt += 1
    elif s == 'L':
        cnt += 0.5

print(round(cnt, ndigits=None))