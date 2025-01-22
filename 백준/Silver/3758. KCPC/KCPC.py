import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 팀개수, 문제개수, 팀아이디, 로그개수
    n, k, t, m = list(map(int, input().split()))
    # 팀별, 문제별 점수 배열
    score = [[0]*k for _ in range(n)]
    # 제출횟수
    cnt = [0]*n
    # 최종 제출 라운드
    latest_submit = [0]*n  

    for r in range(m):
        # 팀번호, 문제번호, 점수
        i, j, s = list(map(int, input().split()))
        cnt[i-1] += 1
        latest_submit[i-1] = r 
        if score[i-1][j-1]:
            score[i-1][j-1] = max(score[i-1][j-1], s) 
        else:
            score[i-1][j-1] = s
    
    total_score = []
    for i in range(n):
        # 점수 높을수록 > 제출횟수 적을수록 > 마지막 제출시간 작을수록
        total_score.append((i+1, sum(score[i]), cnt[i], latest_submit[i]))
    
    # lambda 여러개 하는 방법 검색해봄
    total_score = sorted(total_score, key=lambda x: (-x[1], x[2], x[3]))

    rank = 0
    for i in range(n):
        if total_score[i][0] == t:
            rank = i + 1

    print(rank)