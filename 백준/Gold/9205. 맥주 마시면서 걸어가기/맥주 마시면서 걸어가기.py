import sys 
input = sys.stdin.readline
from collections import deque

def BFS():
    q = deque([[hi, hj]])
    visited = [0]*n
    while q:
        x, y = q.popleft()
        if abs(x-ri) + abs(y-rj) <= 1000:
            print("happy")
            return
        
        for i in range(n):
            if visited[i] == 0:
                nx = conv[i][0]
                ny = conv[i][1]

                if abs(x-nx)+abs(y-ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    print("sad")
    return

T = int(input())
for tc in range(T):
    n = int(input())
    hi, hj = map(int, input().split())
    
    conv = []
    for i in range(n):
        ci, cj = map(int, input().split())
        conv.append((ci, cj))

    ri, rj = map(int, input().split())
    BFS()