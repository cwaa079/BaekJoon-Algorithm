#https://www.acmicpc.net/problem/14889
#스타트와 링크
#combination이용

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

members = [i for i in range(n)]
rand = list(combinations(members, n//2)) #가능한 팀 조합
min_value = 1e9

for i in range(len(rand)//2):
    team = rand[i] #한 조합의 팀원
    p1 = 0
    for j in range(n//2):
        member = team[j] #멤버
        for k in team: #한 조합의 능력치
            p1 += s[member][k]

    team = rand[-i-1] #나머지 조합의 팀원
    p2 = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            p2 += s[member][k]

    val = abs(p1-p2)
    min_value = min(min_value, val)

print(min_value)
