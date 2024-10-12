def find_square(arr):
    # [1] 비상구와 모든 사람간의 가장짧은 가로 또는 세로거리 구하기 => L
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람인 경우
                mn = min(mn, max(abs(ei-i), abs(ej-j))) # 사람과 비상구의 거리 구하기

    # [2] (0,0)부터 순회하면서 길이 L인 정사각형에 비상구와 사람있는지 체크 => 리턴 L+1
    for si in range(N-mn):
        for sj in range(N-mn):
            if si <= ei <= si+mn and sj <= ej <= sj+mn: # 비상구가 포함된 사각형!
                for i in range(si, si+mn+1):
                    for j in range(sj, sj+mn+1):
                        if -11 < arr[i][j] < 0: # 사람인 경우 리턴!
                            return si, sj, mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    ci, cj = map(int, input().split())
    arr[ci-1][cj-1] -= 1 # 같은 곳에 사람이 존재할 수 있음

ei, ej = map(int, input().split())
ei -= 1
ej -= 1
arr[ei][ej] = -11 # 비상구 <= 사람은 10명까지 있기 때문에

ans = 0 # 총 이동 수
cnt = M # 사람 수
for _ in range(K):
    # 출구를 향해서 한칸 이동
    # 출구 도착하면 종료
    narr = [x[:] for x in arr] # deepcopy보다 좋음
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람인 경우
                dist = abs(ei-i) + abs(ej-j) # 현재 비상구까지의 거리
                # 상하 우선
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = i + di, j + dj
                    # 범위 내 + 벽이 아님 (빈칸 or 사람) + 거리가 더 작아야 함
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= 0 and dist > (abs(ei-ni) + abs(ej-nj)):
                        ans += arr[i][j] # 사람들이 이동
                        narr[i][j] -= arr[i][j] # 이동 처리

                        if arr[ni][nj] == -11: # 비상구라면
                            cnt += arr[i][j] # 탈출
                        else:
                            narr[ni][nj] += arr[i][j] # 인원 추가
                        break
    arr = narr

    # 전부 탈출하면 종료
    if cnt == 0:
        break

    # 회전 + 내구도 감소
    si, sj, L = find_square(arr) # 출구와 참가자를 포함한 가장 작은 정사각형
    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-1-j][sj+i] # narr[i][j] = arr[N-j-1][i] : 회전
            if narr[si+i][sj+j] > 0: # 벽이라면
                narr[si+i][sj+j] -= 1 # 내구도 감소
    arr = narr
    ei, ej = find_exit(arr) # 비상구 찾기


print(-ans)
print(ei+1, ej+1) # 최종 비상구 위치