#https://www.acmicpc.net/problem/14890
#경사로
#시뮬레이션 문제(문제 잘 이해하기!!)

import sys
input = sys.stdin.readline

n, l = map(int, input().split()) #크기, 경사로 길이
graph_v = [] #지도

def check(graph):
    now_check = [False for i in range(n)] #한 행별로 경사로의 유무
    for i in range(n-1):
        if graph[i] == graph[i+1]: #같은 값이면 지나갈 수 있음
            continue #다음 거 검사
        if abs(graph[i] - graph[i+1]) > 1: #차이가 1보다 크면
            return False #지나갈 수 없음
        if graph[i] > graph[i+1]: #내리막길
            temp = graph[i+1] #다음값
            for j in range(i+1, i+l+1): #현재값부터 현재값+경사로길이추가한 값까지
                if 0 <= j < n:
                    if graph[j] != temp: return False #연속으로 같은 값이 아니면 x
                    if now_check[j] == True: return False #이미 경사로가 있으면 x
                    now_check[j] = True #경사로존재
                else:
                    return False
        else: #오르막길
            temp = graph[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if graph[j] != temp: return False  # 연속으로 같은 값이 아니면 x
                    if now_check[j] == True: return False  # 이미 경사로가 있으면 x
                    now_check[j] = True  # 경사로존재
                else:
                    return False
    return True

for i in range(n):
    graph_v.append(list(map(int, input().split())))

cnt = 0
#가로방향 확인
for i in range(n):
    if check(graph_v[i]):
        cnt += 1

#세로방향 확인
for i in range(n):
    graph_h = []
    for j in range(n):
        graph_h.append(graph_v[j][i]) #세로방향 한 행
    if check(graph_h):
        cnt += 1

print(cnt)
