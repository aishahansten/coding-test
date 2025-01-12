import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = deque(list(map(int, input().split())))
stack = []
snack_get = []
check = 1

while True:
    if arr[0] == check:
        temp = arr.popleft()
        snack_get.append(temp)
        check = temp + 1

    else:
        if stack:
            if stack[-1] == check:
                temp = stack.pop()
                snack_get.append(temp)
                check = temp + 1
            else:
                temp = arr.popleft()
                stack.append(temp)      
        else:
            temp = arr.popleft()
            stack.append(temp)
    if len(arr) == 0:
        break
    
while stack:
    if snack_get[-1] + 1 == stack[-1]:
        temp = stack.pop()
        snack_get.append(temp)
    else:
        break
    
if stack:
    print("Sad")
else:
    print("Nice")