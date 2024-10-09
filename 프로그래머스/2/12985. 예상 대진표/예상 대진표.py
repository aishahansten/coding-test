def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        if a-b==1 and a%2==0 and b%2 or b-a==1 and b%2==0 and a%2:
            break
            
        if a % 2:
            a = (a+1)//2
        elif a % 2 == 0:
            a //= 2
        if b % 2:
            b = (b+1)//2
        elif b % 2 == 0:
            b //= 2
    return answer