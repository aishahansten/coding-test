def solution(want, number, discount):
    answer = 0
    info = {}
    for i in range(len(want)):
        info[want[i]] = number[i]
        
    for i in range(len(discount)-9):
        cnt = 0 
        copy_info = info.copy()
        for j in range(i, i+10):
            if discount[j] in copy_info and copy_info[discount[j]]>0: 
                copy_info[discount[j]] -= 1
                cnt += 1
            else:
                break
        if cnt == 10:
            answer += 1

    return answer