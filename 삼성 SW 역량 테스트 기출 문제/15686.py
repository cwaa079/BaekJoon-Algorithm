#https://www.acmicpc.net/problem/15686
#치킨배달
#시간복잡도가 작아서 조합으로 풀 수 있었던 시뮬레이션 문제

from itertools import combinations

n, m = map(int, input().split()) #크기, 치킨집개수
house = [] #집이 있는 좌표
chicken = [] #치킨집이 있는 좌표
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 2: #치킨집
            chicken.append([i+1, j+1])
        elif data[j] == 1: #집
            house.append([i+1, j+1])

cans = list(combinations(chicken, m))

def get_sum(can):
    total = 0
    for hx, hy in house:
        street = 1e9
        for cx, cy in can:
            street = min(street, abs(hx-cx)+abs(hy-cy)) #집마다의 치킨거리 최소값
        total += street #도시의 치킨거리
    return total

city_st = 1e9
for can in cans:
    city_st = min(city_st, get_sum(can))

print(city_st)
