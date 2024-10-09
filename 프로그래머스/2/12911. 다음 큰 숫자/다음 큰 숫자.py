def solution(n):
    answer = 0
    for num in range(n+1, 1000001):
        bin_n = bin(n)[2:]
        bin_num = bin(num)[2:]
        n1 = str(bin_n).count("1")
        n2 = str(bin_num).count("1")
        if n1 == n2:
            answer = num
            break
        
    return answer