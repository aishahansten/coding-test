import sys
input = sys.stdin.readline

ans = []
for i in range(5):
    name = input().rstrip()
    for j in range(len(name)-3+1):
        if name[j:j+3] == 'FBI':
            ans.append(i+1)

            break
if len(ans)>0:
    print(*ans)
else:
    print("HE GOT AWAY!")