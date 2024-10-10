n = int(input())  # 휴가 일수
jobs = [list(map(int, input().split())) for _ in range(n)]

# DP 배열 초기화
dp = [0] * (n + 1)

# 마지막 날부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    t, p = jobs[i]
    if i + t <= n:
        dp[i] = max(dp[i + 1], p + dp[i + t])  # 일을 하는 경우와 안 하는 경우 비교
    else:
        dp[i] = dp[i + 1]  # 일을 못하는 경우, 다음 날로 넘김

# 최대 수익 출력
print(dp[0])