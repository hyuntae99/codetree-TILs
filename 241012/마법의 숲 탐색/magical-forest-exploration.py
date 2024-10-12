from collections import deque

di = [-1,0,1, 0]
dj = [0, 1,0,-1]

def bfs(si, sj):
    q = deque()
    v = [[0] * (C+2) for _ in range(R+4)]

    q.append((si,sj))
    v[si][sj] = 1
    mx_i= 0 # 최대 깊이를 구하기 위해서

    while q:
        ci, cj = q.popleft() # 현재 위치
        mx_i = max(mx_i, ci)

        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 4방향 탐색
            ni, nj = ci + di, cj + dj
            # 범위 내 + 미방문 + 로봇 내 이동 or 출구 -> 상대 골렘으로
            if not v[ni][nj] and (arr[ci][cj] == arr[ni][nj] or ((ci, cj) in exits and arr[ni][nj] >= 2)):
                q.append((ni,nj))
                v[ni][nj] = 1

    return mx_i - 2

R, C, K =  map(int, input().split())
units = [list(map(int, input().split())) for _ in range(K)]
arr = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
exits = set()
num = 2 # 로봇은 2 ~ K+2 버전까지
ans = 0

for cj, dr in units:
    ci = 1  # 시작 높이
    while True:
        # 다리, 양팔 모두 이동 가능하다면 하강
        if (arr[ci+2][cj] + arr[ci+1][cj+1] + arr[ci+1][cj-1]) == 0:
            ci += 1 # 하강
        # 왼쪽 이동시 머리, 왼팔, 다리 + 왼쪽 아래 이동시 왼팔, 다리 확인
        elif (arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-1] + arr[ci+1][cj-2] + arr[ci+2][cj-1]) == 0:
            cj -= 1 # 왼쪽 이동
            ci += 1 # 하강
            dr = (dr - 1) % 4 # 왼쪽 회전
        # 오른쪽 이동시 머리, 오른팔, 다리 + 오른쪽 아래 이동시 오른팔, 다리 확인
        elif (arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1] + arr[ci+1][cj+2] + arr[ci+2][cj+1]) == 0:
            cj += 1 # 오른쪽 이동
            ci += 1 # 하강
            dr = (dr + 1) % 4  # 오른쪽 회전
        else:
            break
    # 골렘이 장외일 경우
    if ci < 4:
        arr = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)] # 배열 초기화
        num = 2
        exits = set()
    else: # 장외인 경우 처리 x
        # 방문 처리
        arr[ci-1][cj] = arr[ci+1][cj] = num # 머리, 다리
        arr[ci][cj-1] = arr[ci][cj] = arr[ci][cj+1] = num # 몸통
        num += 1
        exits.add((ci + di[dr], cj + dj[dr])) # 출구 저장

        ans += bfs(ci, cj) # 최종 골렘 위치에서 하차

print(ans)