import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
num = A*B*C

cnt = [0]*10
for i in range(len(str(num))):
    temp = num % 10
    num //= 10
    cnt[temp] += 1

print(*cnt, sep='\n')
