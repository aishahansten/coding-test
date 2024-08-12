import sys
input = sys.stdin.readline

N = int(input())


ans = []
visited = [False] * (N+1)
def backtracking():
    if len(ans) == N:
        print(*ans)
        return
        
    for i in range(1,N+1):
        if not visited[i] and i not in ans:
            ans.append(i)
            backtracking()
            ans.pop()
            
backtracking()
