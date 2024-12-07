N = int(input())
budget = list(map(int, input().split()))
total = int(input())
# 485
ans = 0
# 121

start, end = 0, max(budget)

while start<=end:
    avg = (start+end)//2

    temp = 0
    for b in budget:
        if b <= avg:
            temp += b
        else:
            temp += avg

    if temp > total:
        end = avg - 1
     
    else:
        ans = avg
        start = avg + 1
print(ans)