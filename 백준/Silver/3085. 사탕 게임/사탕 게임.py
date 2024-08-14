import sys
input = sys.stdin.readline

def max_continuous_length(board, N):
    max_length = 1
    # 행에서 최대 연속 길이 계산
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                temp += 1
                max_length = max(max_length, temp)
            else:
                temp = 1
    
    # 열에서 최대 연속 길이 계산
    for j in range(N):
        temp = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                temp += 1
                max_length = max(max_length, temp)
            else:
                temp = 1
    
    return max_length

N = int(input())
board = [list(input().strip()) for _ in range(N)]

ans = 1
for i in range(N):
    for j in range(N-1):
        # 오른쪽으로 비교
        if j + 1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, max_continuous_length(board, N))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래로 비교
        if i + 1 < N and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, max_continuous_length(board, N))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)
