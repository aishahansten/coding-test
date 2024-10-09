from collections import deque

def find(begin, target, words):
    visited = [0]*(len(words))
    q = deque()
    q.append((begin, 0))
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt

        
        for w in range(len(words)):
            temp_cnt = 0
            if not visited[w]:
                for j in range(len(begin)):
                    if now[j] != words[w][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    visited[w] = 1
                    q.append((words[w], cnt+1))

def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
    else:
        answer = find(begin, target, words)
    return answer