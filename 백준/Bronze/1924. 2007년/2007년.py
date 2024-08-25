import sys
input = sys.stdin.readline

x, y = map(int, input().split())

day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
days = 0

num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(x-1):
    days += num_days[i]

days = (days+y)%7
print(day_list[days])