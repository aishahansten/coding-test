import sys
input = sys.stdin.readline

A, B = map(int, input().split())

# x2 를 했다면 맨 끝자리가 1일수가 없다

def findA(B, cnt):

    if B == A:
        cnt += 1
        print(cnt)
        return
     
    elif B < A:
        print(-1)
        return
      
    else:
        if B % 10 == 1:
            B //= 10
            # print('la', cnt)
            cnt += 1
            findA(B, cnt)

        elif B % 2 == 0:
            B //= 2
            # print('do', cnt)
            cnt += 1
            findA(B, cnt)
        else:
            print(-1)
            return
        

        

 

findA(B, 0)

