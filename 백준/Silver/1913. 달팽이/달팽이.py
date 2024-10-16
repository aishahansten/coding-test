import sys
input = sys.stdin.readline

N = int(input())
find = int(input())
find_idx = []
# 시계방향 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0]*N for _ in range(N)]
si, sj = N//2, N//2
num = 1
width = 0

arr[si][sj] = num

for turn in range(N//2+1):
    for i in range(4):
        for j in range(width):
            si += dx[i]
            sj += dy[i]
            num += 1
            arr[si][sj] = num
            if num == find:
                find_idx = [si+1, sj+1]

    # 마지막위치 arr[0][0]에 도달하면 끝내기
    if si == 0 and sj == 0:
        break
    
    # 원으로 생각하면 왼쪽 위가 시작점으로 하면 width 만큼씩 dx, dy 반복
    si -= 1
    sj -= 1
    width += 2    

for a in arr:
    print(*a)
if find == 1:
    find_idx = [N//2+1, N//2+1]
    print(*find_idx)
else:
    print(*find_idx)

