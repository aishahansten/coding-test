import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# M 개 치킨집 지정

# 1. 치킨집 위치 파악
chickens = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))
# print(chickens)

# 2. M 개 치킨집 조합
comb_chicken = list(combinations(chickens, M))

# stores = []
# visited = [False]*len(chickens)
# def combination(stores):
#     global comb_chicken
#     if len(stores) == M:
#         comb_chicken.append(stores[:])
#         return
   
#     for i in range(len(chickens)):
#         if visited[i]:
#             continue
#         stores.append(chickens[i])
#         visited[i] = True
#         combination(stores)
#         stores.pop()
#         visited[i] = False

# combination(stores)
# print(comb_chicken)


# findmin = [0]*len(comb_chicken)
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
    # findmin[i] = temp

# min 출력
print(ans)