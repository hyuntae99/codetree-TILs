from collections import  deque

# 공 방향 우,상,좌,하
ddi = [0,-1, 0, 1]
ddj = [1, 0,-1, 0]

def bfs(ci,cj,team_n):
    team = deque()
    q = deque()
    v[ci][cj] = 1
    arr[ci][cj] = team_n # 팀 번호로 변환
    q.append((ci,cj))
    team.append((ci,cj))

    while q:
        si, sj = q.popleft()  # 현재 위치
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 4방향 탐색
            ni, nj = si + di, sj + dj
            # 미방문 + 범위 내 + 2, 3이면
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[ni][nj] in (2, 3):
                v[ni][nj] = 1
                q.append((ni,nj))
                team.append((ni,nj))
                arr[ni][nj] = team_n # 팀 번호로 변환
    teams[team_n] = team # 팀 번호에 순서대로 저장

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * N for _ in range(N)]
ans = 0
team_n = 5 # 팀 번호
teams = {} # 찾을 때 5 더하자!
for i in range(N):
    for j in range(N):
        if v[i][j] == 0 and arr[i][j] == 1: # 머리 위치인 경우
            bfs(i,j,team_n)
            team_n += 1

# 라운드 진행
for k in range(K):
    # 머리 방향으로 이동
    for team in teams.values(): # 순서대로 좌표
        ei, ej = team.pop() # 꼬리 좌표 삭제
        arr[ei][ej] = 4 # 복구
        ci, cj = team[0] # 머리 좌표
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 4방향 탐색
            ni, nj = ci + di, cj + dj
            # 범위 내 + 4를 만나야 함
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 4:
                team.appendleft((ni,nj)) # 머리 좌표에 등록
                arr[ni][nj] = arr[ci][cj] # 이전 번호 이어받기
                break

    # 공 방향 설정
    dr = (k // N) % 4 # 방향
    start = k % N # 위치

    if dr == 0:
        ci, cj = start, 0
    elif dr == 1:
        ci, cj = N-1, start
    elif dr == 2:
        ci, cj = N-start-1, N-1
    else:
        ci, cj = 0, N-start-1

    # 맞으면 점수 오르고 교체
    for _ in range(N):
        # 범위 안 + 특정 팀을 만났을 때
        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj] > 4:
            team_n = arr[ci][cj] # 팀 번호
            ans += (teams[team_n].index((ci,cj)) + 1) ** 2 # 몇번 째인지 찾고 그에 맞는 점수 획득
            teams[team_n].reverse()
            break
        ci, cj = ci + ddi[dr], cj + ddj[dr]
print(ans)