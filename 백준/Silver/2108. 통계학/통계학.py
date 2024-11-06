import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

# 최빈값 count
count_list = [0]*8001

for n in numbers:
    count_list[n+4000] += 1

# 최빈값의 개수 most_cnt
most_cnt = max(count_list)
arr = []
for c in range(len(count_list)):
    if count_list[c] == most_cnt:
        arr.append(c-4000)

ans1 = round(sum(numbers)/N, ndigits=None)
ans2 = numbers[N//2]
if len(arr) == 1:
    ans3 = arr[0]
else:
    ans3 = arr[1]
ans4  = numbers[-1]-numbers[0]

print(ans1)
print(ans2)
print(ans3)
print(ans4)
