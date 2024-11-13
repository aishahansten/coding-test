N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

    
def is_same(size):
    for i in range(N-size+1):
        for j in range(M-size+1):
            if arr[i][j] == arr[i][j+size-1] == arr[i+size-1][j] == arr[i+size-1][j+size-1]:
                return True
            
start = min(N, M)

for k in range(start, 0, -1):
    if is_same(k):
        print(k**2)
        break


