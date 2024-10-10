from itertools import permutations

# 입력 받기
n = int(input())

# 1부터 n까지의 숫자를 사용한 모든 순열을 구하기
arr = permutations(range(1, n + 1))

# 각 순열을 출력하기
for a in arr:
    print(" ".join(map(str, a)))