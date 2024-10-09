from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    print(len(q))
    for k in range(len(s)):
        stack = [q[0]]
        for i in range(1, len(q)):
            stack.append(q[i])
            if len(stack)>=2 and (stack[-2]=='['and stack[-1]==']' or stack[-2] =='{' and stack[-1]=='}' or stack[-2] == '(' and stack[-1] == ')'):
                stack.pop()
                stack.pop()
        if len(stack)==0:
            answer += 1
            stack = []
                
        q.append(q.popleft())
    
    return answer