from itertools import permutations

# 입력 받기
n = int(input())

cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

# 최소 비용을 무한대로 초기화
min_cost = float('inf')

# 1번 지점을 제외한 나머지 지점들의 순열을 구함
for perm in permutations(range(1, n)):
    current_cost = 0
    start = 0 

    for i in perm:
        current_cost += cost[start][i]
        start = i
    
    # 마지막에서 다시 1번 지점으로 돌아오는 비용 추가
    current_cost += cost[start][0]
    
    min_cost = min(min_cost, current_cost)

print(min_cost)