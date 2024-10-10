def generate_combinations(current_combination, n, k):
    if len(current_combination) == n:
        print(" ".join(map(str, current_combination)))
        return
    
    for i in range(1, k + 1):
        generate_combinations(current_combination + [i], n, k)

# 입력 받기
k, n = map(int, input().split())

# 순서쌍 생성 함수 호출
generate_combinations([], n, k)