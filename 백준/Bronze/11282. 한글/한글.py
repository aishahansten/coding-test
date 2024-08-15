import sys
input = sys.stdin.readline

N = int(input())
# 한글 아스키 코드 '가' 44032 ~ '힣' 55203
print(chr(N + 44032 - 1))