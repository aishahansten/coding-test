import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    order = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        arr = deque()

    cnt_rev = 0
    for p in order:
        
        if p == "R":
            cnt_rev += 1

        elif p == "D":
            if len(arr) == 0:
                arr = "error"
                break
            else:
                if cnt_rev % 2 == 0:
                    arr.popleft()   
                else:
                    arr.pop()
    if arr == "error":
        print(arr)
    else:
        if cnt_rev % 2 == 0:

            print(f"[{','.join(arr)}]")
        else:
            arr.reverse()
            print("["+','.join(arr)+"]")

    