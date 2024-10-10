# 변수 선언 및 입력
n = int(input())
ans = 0
seq = []

# 아름다운 수인지 확인하는 함수
def is_beautiful():
    i = 0
    while i < n:
        # 현재 숫자만큼 연속된 숫자가 존재하는지 확인
        if i + seq[i] > n:  # 범위를 벗어나면 False
            return False
        
        # 연속되는 구간이 모두 동일한 숫자인지 확인
        if seq[i:i + seq[i]] != [seq[i]] * seq[i]:
            return False
        
        i += seq[i]  # 다음 연속된 숫자 확인을 위해 i 증가
        
    return True

# 아름다운 수의 개수를 세는 함수
def count_beautiful_seq(cnt):
    global ans
    
    if cnt == n:  # 길이가 n인 수열을 완성했을 때
        if is_beautiful():  # 아름다운 수인지 확인
            ans += 1
        return
    
    # 1부터 4까지의 숫자를 사용하여 재귀적으로 수열을 생성
    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()

# 아름다운 수 계산 시작
count_beautiful_seq(0)
print(ans)