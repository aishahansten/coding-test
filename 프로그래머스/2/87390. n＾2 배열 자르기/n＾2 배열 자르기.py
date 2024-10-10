def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row = i//n
        column = i%n
        answer.append(max(row, column)+1)
        
    return answer