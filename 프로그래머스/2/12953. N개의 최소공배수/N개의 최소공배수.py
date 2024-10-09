def solution(arr):
    answer = 0
    arr.sort(reverse = True)
    d = 1
    flag = 0
    while True:
        
        answer = arr[-1]*d
        for i in range(len(arr)-2, -1, -1):
            if answer % arr[i]:
                flag = 0
                break
            flag = 1
            
        if flag:
            break
        else:
            d += 1
    return answer