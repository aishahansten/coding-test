import sys 
input = sys.stdin.readline

K = int(input())

multi = 0
for i in range(50):
    if 2**i >= K:
        multi = i 
        break

ans1 = 2**multi
print1 = ans1
count = 0

if K == ans1:
    count = 0

else:
    while K>0:
        if ans1 > K:
            ans1 //= 2
            count += 1
        elif ans1 <= K:
            K -= ans1

ls = [print1, count]
print(*ls)