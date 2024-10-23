import sys
input = sys.stdin.readline

N = int(input())
column = []

# 입력을 받음
for _ in range(N):
    L, H = map(int, input().split())
    column.append([L, H])

# 위치 순서대로 정렬
column.sort()

# 최대 높이 찾기
max_height = 0
max_index = 0

for i in range(N):
    if column[i][1] > max_height:
        max_height = column[i][1]
        max_index = i

# 왼쪽 부분 계산
total = 0
left_max_height = column[0][1]
left_max_position = column[0][0]

for i in range(1, max_index + 1):
    if column[i][1] > left_max_height:
        total += (column[i][0] - left_max_position) * left_max_height
        left_max_height = column[i][1]
        left_max_position = column[i][0]

total += max_height  # 최대 높이 부분 더해주기

# 오른쪽 부분 계산
right_max_height = column[-1][1]
right_max_position = column[-1][0]

for i in range(N-2, max_index - 1, -1):
    if column[i][1] > right_max_height:
        total += (right_max_position - column[i][0]) * right_max_height
        right_max_height = column[i][1]
        right_max_position = column[i][0]

# 마지막 남은 부분 면적 더해주기
total += (right_max_position - column[max_index][0]) * right_max_height

print(total)
