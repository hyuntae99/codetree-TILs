import math

n = int(input()) # 식당 수
customers = list(map(int, input().split())) # 각 식당의 고객 수
LDR, MBR = map(int, input().split()) # 팀장과 사원의 능력

members = []
for customer in customers:
    rest = customer - LDR
    if rest <= 0:
        members.append(0)
    else:
        member = rest / MBR
        if member != maht.ceil(member):
            members.append(maht.ceil(member))
        else:
            members.append(int(member))

print(max(members) + 1)