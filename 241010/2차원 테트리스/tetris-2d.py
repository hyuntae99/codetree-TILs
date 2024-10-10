# k: 블록 입력 횟수
k = int(input())

# 6x4 크기의 게임판 (False는 빈 칸, True는 블록이 있는 칸)
one = [[False] * 4 for _ in range(6)]  # 90도 회전 전 (노란색 보드)
two = [[False] * 4 for _ in range(6)]  # 90도 회전 후 (빨간색 보드)

# 점수 변수
score = 0

# 블록을 배치하고 시뮬레이션하는 함수
def simulate(t, x, y, target):
    # 블록이 도착할 위치를 찾음
    sx, sy = find_drop_position(t, x, y, target)

    # 블록을 안착시킴
    place_block(t, sx, sy, target)

    # 행을 검사하여 꽉 찬 행을 삭제하고 중력 처리
    for ty in range(sy, -1, -1):
        while is_row_full(ty, target):
            remove_row(ty, target, False)
            apply_gravity(ty, target)

    # 연한 부분(2행 이하)에 있는 블록 처리
    handle_light_area(target)

# 블록을 게임판에 놓는 함수
def place_block(t, x, y, target):
    if t == 1:  # 1x1 블록
        target[y][x] = True
    elif t == 2:  # 1x2 블록 (가로)
        target[y][x] = True
        target[y][x + 1] = True
    elif t == 3:  # 2x1 블록 (세로)
        target[y][x] = True
        target[y - 1][x] = True

# 연한 부분(상단 2행)에 블록이 있는 경우 처리하는 함수
def handle_light_area(target):
    over_count = 0

    # 상단 2행에서 블록이 있는지 카운팅
    for y in range(2):
        for x in range(4):
            if target[y][x]:
                over_count += 1
                break

    # 연한 부분에 블록이 있는 경우 그만큼 아래 행을 삭제함
    for _ in range(over_count):
        remove_row(5, target, True)
        apply_gravity(5, target)

# 특정 행을 삭제하는 함수
def remove_row(y, target, is_light_row):
    global score

    for x in range(4):
        target[y][x] = False

    if not is_light_row:
        score += 1  # 꽉 찬 행을 삭제했을 때만 점수 추가

# 블록을 한 칸씩 아래로 내리는 함수
def apply_gravity(start_row, target):
    for y in range(start_row, 0, -1):
        target[y] = target[y - 1][:]
    target[0] = [False] * 4  # 최상단 행을 빈 상태로 초기화

# 행이 가득 찼는지 확인하는 함수
def is_row_full(y, target):
    return all(target[y])

# 남은 블록의 수를 출력하는 함수
def print_remaining_blocks():
    remaining_blocks = sum(sum(row) for row in one[2:]) + sum(sum(row) for row in two[2:])
    print(remaining_blocks)

# 블록이 떨어질 위치를 찾는 함수
def find_drop_position(t, x, y, target):
    for drop_y in range(6):
        if t == 1 and target[drop_y][x]:  # 1x1 블록
            return [x, drop_y - 1]
        elif t == 2 and (target[drop_y][x] or target[drop_y][x + 1]):  # 1x2 블록
            return [x, drop_y - 1]
        elif t == 3 and target[drop_y][x]:  # 2x1 블록
            return [x, drop_y - 1]
    return [x, 5]

# 블록을 90도 회전하는 함수
def rotate_block(t, x, y):
    if t == 1:
        return (1, 3 - y, x)  # 1x1 블록은 회전 후 그대로
    elif t == 2:
        return (3, 3 - y, x)  # 1x2 블록
    elif t == 3:
        return (2, 3 - (y + 1), x)  # 2x1 블록

# 입력 처리 및 블록 배치
for _ in range(k):
    t, y, x = map(int, input().split())
    simulate(t, x, y, one)  # 원래 방향으로 시뮬레이션 ()
    rotated_t, rotated_x, rotated_y = rotate_block(t, x, y) # 90도 회전
    simulate(rotated_t, rotated_x, rotated_y, two)  # 90도 회전한 방향으로 시뮬레이션

# 결과 출력
print(score)
print_remaining_blocks()