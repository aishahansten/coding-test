def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            x = i
            y = yellow // i
        if x + y == (brown-4)//2 and x >=y:
            answer = [x+2, y+2]
    
    return answer
