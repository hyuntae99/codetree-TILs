# 제초제의 경우 k의 범위만큼 대각선으로 퍼지며, 벽이 있는 경우 가로막혀서 전파되지 않습니다.
# 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
# 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식이 되며, 나눌 때 생기는 나머지는 버립니다.
# 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
# c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
# 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.
# 성장 -> 번식 -> 위치 선정 및 제초

INF = -100000000 # 벽
N, M, K, C = map(int, input().split()) # 맵 크기, 시간, 제초제 범위, 제초제 유지
C = -(C+1) # 제초제 유지 기간

# 초기 배열 설정 (벽으로 둘러싸인 숲)
arr = [[INF] * (N+2)]
for i in range(N):
    a = list(map(int, input().split()))
    a.insert(0, INF)  # 리스트 앞에 0 추가
    a.append(INF)  # 리스트 뒤에 0 추가
    arr.append(a)
arr.append([INF] * (N+2))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == -1:
            arr[i][j] = INF       # 건물(벽)을 영구적인 제초제 저리

ans = 0
for _ in range(M): # M년 간 진행
    # [0] 1년의 시작 (제초제 감소)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] < 0:  # 제초제가 뿌려져 있다면 감소 (건물은 -100000 이므로 절대 0 되지 않음)
                arr[i][j] += 1

    # [1] 인접한 네칸 중 나무있는 칸 수만큼 동시에 성장
    narr = [x[:] for x in arr] # 배열 복사
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0:  # 나무가 있다면, 인접 나무수만큼 성장
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)): # 주변 탐색
                    if arr[ni][nj] > 0:
                        narr[i][j] += 1
    arr = narr

    # [2] 인접한 빈칸에 번식(나무수//빈칸수 => 동시)
    narr = [x[:] for x in arr]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0:  # 내가 나무면 번식
                tlst = []  # 빈칸 좌표 저장
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)): # 주변 탐색
                    # 0인 좌표 찾기
                    if arr[ni][nj] == 0:
                        tlst.append((ni, nj))
                if len(tlst) > 0:  # 빈칸이 있는 경우 => 번식
                    d = arr[i][j] // len(tlst) # 나눌 수 있는 만큼 번식
                    for ti, tj in tlst:
                        narr[ti][tj] += d
    arr = narr

    # [3-1] 가장 많이 박멸되는 칸을 찾기
    mx, mx_i, mx_j = 0, 0, 0 # 박멸된 수, 좌표
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0:  # 나무 있는 칸에 뿌려야 제초제 확산됨
                cnt = arr[i][j]  # 내 자리(중심) 포함
                for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)): # 대각선 방향
                    for mul in range(1, K + 1):  # K만큼 뻗어가면서 처리
                        ni, nj = i + di * mul, j + dj * mul
                        if arr[ni][nj] <= 0:  # 빈땅, 제초제, 건물
                            break  # 그 방향은 그만!
                        else:  # 나무 있는 경우
                            cnt += arr[ni][nj]
                # 최대값이면 갱신
                if mx < cnt:
                    mx, mx_i, mx_j = cnt, i, j
    if mx == 0:  # 0이라면 나무가 한 그루도 없는것! => break
        break
    ans += mx

    # [3-2] 제초제 살표
    # 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우,
    # 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다
    arr[mx_i][mx_j] = C  # 최적의 자리에 제초제 뿌림
    for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)): # 주변 탐색
        for mul in range(1, K + 1):  # 뻗어가면서 처리
            ni, nj = mx_i + di * mul, mx_j + dj * mul
            # 벽(건물)에 제초제 뿌리면 건물이 시간지나면 빈땅이됨!!!
            if arr[ni][nj] <= 0:  # 뻗어가는것이 종료되는 조건: 빈땅, 제초제뿌려진 빈땅, 벽(건물)을 제외!!
                if C <= arr[ni][nj]:  # 제초제 뿌리는 조건
                    arr[ni][nj] = C  # 뿌리고
                break
            else:  # 나무면
                arr[ni][nj] = C
print(ans)