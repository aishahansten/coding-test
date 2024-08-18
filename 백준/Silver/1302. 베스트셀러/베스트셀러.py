import sys
input = sys.stdin.readline

N = int(input())
check = dict()
for _ in range(N):
    name = input().strip()
    if name in check:
        check[name] += 1
    else:
        check[name] = 1

maxvalue = max(check.values())
list = []
for item in check:
    if check[item] == maxvalue:
        list.append(item)
list.sort()
print(list[0])
