def solution(k, tangerine):
    answer = 0
    info = {}
    
    for t in tangerine:
        if t in info:
            info[t]+=1
        else:
            info[t] = 1
    
    info = dict(sorted(info.items(), key = lambda x:x[1], reverse=True))
    for i in info:
        if k <= 0:
            break
        k -= info[i]
        answer += 1
    return answer
