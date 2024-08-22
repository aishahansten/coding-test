import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# M 개 치킨집 지정

chickens = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

# M 개 치킨집 조합
# comb_chicken = list(combinations(chickens, M))
comb_chicken = []
stores = []
idx = 0
def combination(stores, idx):
    if len(stores) == M:
        comb_chicken.append(stores[:])
        return
   
    for i in range(idx, len(chickens)):
        stores.append(chickens[i])
        combination(stores, i + 1)
        stores.pop()
    
combination(stores, idx)

# 치킨거리 최솟값 계산
def findMin(chickenstores):
    totalminlength = 0
    for hx, hy in house:
            minlength = int(1e9)
            for store in chickenstores:
                ci, cj = store
                far = abs(ci-hx)+abs(cj-hy)
                if far < minlength:
                    minlength = far
            totalminlength += minlength
    return totalminlength

ans = int(1e9)
for i in range(len(comb_chicken)):
    temp = findMin(comb_chicken[i])
    if temp < ans:
        ans = temp

print(ans)