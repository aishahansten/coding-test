import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
durability = deque(list(map(int, input().split())))
is_robot = deque([False]*N) # 내리는 위치 이후는 로봇 있을수 없음.

turn = 0

while True:
    
    # 1. 회전하기
    '''
    temp = durability[-1] 
    for i in range(2*N-2, -1, -1):
        durability[i+1] = durability[i]
    durability[0] = temp

    for j in range(N-2, -1, -1):
        is_robot[j+1] = is_robot[j]
    is_robot[0] = False
    '''
    durability.rotate(1)
    is_robot.rotate(1)

    # 내리는위치는 항상 내려줌
    if is_robot[N-1]:
        is_robot[N-1] = False

    # 2. 가장 먼저 올라간 로봇부터 위치 옮기기
    
    for k in range(N-2, -1, -1):
        if is_robot[k] == True and is_robot[k+1] == False and durability[k+1]>=1:
            is_robot[k] = False
            is_robot[k+1] = True
            durability[k+1] -= 1

    # 내리는위치 항상 내려줌
    if is_robot[N-1] == True:
        is_robot[N-1] = False
                 
    #3. 새 로봇 올리기

    if is_robot[0] == False and durability[0] >= 1:
        durability[0] -= 1
        is_robot[0] = True

    turn += 1
    # 5. 
  
    if durability.count(0) >= K:
        break
    
print(turn)