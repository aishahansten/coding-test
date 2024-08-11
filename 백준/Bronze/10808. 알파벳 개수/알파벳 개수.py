import sys
input = sys.stdin.readline

S = input().rstrip()
alpha = [0] * 26

for s in S:
    alpha[ord(s)-97] += 1
    
print(*alpha)