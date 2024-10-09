from collections import deque
def solution(elements):
    answer = set()
    
    q = deque(elements)
    for i in range(len(q)):
        sum = 0
        for j in q:
            sum += j
            answer.add(sum)
        q.append(q.popleft())
    
    
    
    
    return len(answer)