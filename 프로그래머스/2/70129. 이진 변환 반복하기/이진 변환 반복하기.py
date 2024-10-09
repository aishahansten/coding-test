def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    
    while True:
        if s == "1":
            break
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt += 1
        
    answer = [cnt, zero_cnt]
    return answer