import sys

input= sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

amount = 0

for i in range(1, W-1):
    leftmax = max(height[:i])
    rightmax = max(height[i+1:])
    smaller_value = min(leftmax, rightmax)

    if smaller_value > height[i]:
        amount += (smaller_value-height[i])

print(amount)
