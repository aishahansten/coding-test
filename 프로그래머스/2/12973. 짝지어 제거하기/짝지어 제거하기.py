def solution(s):
    answer = -1
    stack = []
    for c in s:
        stack.append(c)
        if len(stack)>=2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if len(stack) != 0:
        answer = 0
    else:
        answer = 1

    return answer