import sys
input=sys.stdin.readline

string = input().rstrip()
fstring = input().rstrip()
fstring = list(fstring)
check = []

for char in string:
    check.append(char)

    if check[-len(fstring):] == fstring:
        for l in range(len(fstring)):
            check.pop()

if check:
    print(''.join(check))
else:
    print("FRULA")
