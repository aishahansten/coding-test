import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split()) 
seqNo = list(map(int, input().split()))
que = deque([i for i in range(1, N+1)])

def calcOne(q):
    q.popleft()

def calcTwo(q):
    temp = q.popleft()
    q.append(temp)

def calcThree(q):
    temp = q.pop()
    q.appendleft(temp)

cnt = 0
for num in seqNo:
    while True: 

        if que[0] == num:
            calcOne(que)
            break
        
        else:
            idx = que.index(num)
            if len(que) / 2 > idx:
                while que[0] != num:
                    calcTwo(que)
                    cnt += 1
         
            else:
                while que[0] != num:
                    calcThree(que)
                    cnt += 1
   
                 
              
        
print(cnt)
'''
idx = que.index(seqNo[0])
templist = str(que)
idx2 = templist.find(str(seqNo[0]))

print(idx, templist, str(seqNo[0]), idx2)
0 deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 1 7
idx 는 리스트의 인덱스 반환
idx2 는 문자열로 변환했을 때 d, e, q, u, e, (, [, 1 즉 7 반환
'''