import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_length =int(1e9)

start = 0
end = 0
tempsum = arr[0]


while start <= end:
    if tempsum < S:
        
        if end == N-1: # 이미 끝까지 왔는데 S보다 작음
            break
        end += 1
        tempsum += arr[end]

    elif tempsum >= S: # S 이상일 때
        min_length = min(min_length, end-start+1)
        start += 1
        tempsum -= arr[start-1]

if min_length != int(1e9):
    print(min_length)
    
else:
    print(0)