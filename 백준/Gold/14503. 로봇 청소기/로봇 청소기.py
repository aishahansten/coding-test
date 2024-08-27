import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
status = [list(map(int, input().split())) for _ in range(N)]
# 0: 청소x 빈칸 1 : 벽
#0:북 1:동 2:남 3:서 => 반시계는 북서남동 0321
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[False]*M for _ in range(N)]

cnt = 1
visited[r][c] = True

while True:
    flag = 0 # 4칸 중 청소되지 않은 빈 칸이 없는 경우
    for _ in range(4):
        nx = r + dx[(d+3)%4] 
        ny = c + dy[(d+3)%4]
        d = (d+3)%4

        if 0 <= nx < N and 0 <= ny < M and status[nx][ny] == 0:
            if not visited[nx][ny]:
         
                visited[nx][ny] = True
                r = nx
                c = ny
             
                cnt += 1
                flag = 1
                break
    
    if flag == 0:
        if status[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]