import sys 
input = sys.stdin.readline

N = int(input())
power = list(map(int, input().split()))
power.sort()
sum = []
for i in range(len(power)//2):
    temp = power[i] + power[len(power)-1-i]
    sum.append(temp)
ans = min(sum)
print(ans)
