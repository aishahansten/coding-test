def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
    if len(stack) != 0:
        answer = False
    return answer
   