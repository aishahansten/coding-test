def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_num = i
        d = i + 1
        while sum_num <= n:
            if sum_num == n:
                answer += 1
                break
            sum_num += d
            d += 1
    return answer