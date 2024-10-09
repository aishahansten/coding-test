def solution(n):
    dp = [0]*100001
    dp[0] = 0
    dp[1] = 1
    for k in range(2, 100001):
        dp[k] = dp[k-1] + dp[k-2]
    nth = dp[n]
    answer = nth%1234567
    return answer