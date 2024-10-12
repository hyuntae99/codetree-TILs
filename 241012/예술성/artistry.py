from collections import deque

def bfs(ci,cj):
    q = deque()
    v[ci][cj] = 1
    q.append((ci,cj))
    groups[-1].add((ci,cj)) # 그룹 초기 값

    while q:
        si, sj = q.popleft() # 현재 위치
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)): # 4방향 탐색
            ni, nj = si + di, sj + dj
            # 범위 내 + 미방문 + 같은 숫자끼리
            if 0 <= ni < n and 0 <= nj < n and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = 1
                groups[-1].add((ni,nj)) # 그룹 추가


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 4번의 예술 점수를 구해야 함
for time in range(4):
    # 예술 점수 구하기 : 그룹 나누고 2개 그룹의 점수 누적
    v = [[0] * n for _ in range(n)]
    groups = []
    nums = []
    for i in range(n):
        for j in range(n):
            if not v[i][j]: # 미방문이면
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i,j)

    CNT = len(nums)
    for i in range(CNT-1):
        for j in range(i+1, CNT):
            cnt = 0
            point = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for ci, cj in groups[i]: # 1번 그룹에서 4방향 탐색
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = ci + di, cj + dj
                    if (ni, nj) in groups[j]: # 인접한 좌표가 j에 있는가
                        cnt += 1
            ans += (point * cnt) # 그룹 간 예술 점수

    if time == 3:
        break

    # 회전 : 십자가 반시계, 부분 사각형 시계
    narr = [[0] * n for _ in range(n)]
    M = n // 2 # 중앙 인덱스
    # 십자가 부분 시계 방향
    for i in range(n):
        narr[M][i] = arr[i][M]
    for j in range(n):
        narr[j][M] = arr[M][n - j - 1]

    for (si, sj) in ((0, 0), (0, M + 1), (M + 1, 0), (M + 1, M + 1)):
        for i in range(M):
            for j in range(M):
                narr[si + i][sj + j] = arr[si + M - j - 1][sj + i]
    arr = narr


print(ans)