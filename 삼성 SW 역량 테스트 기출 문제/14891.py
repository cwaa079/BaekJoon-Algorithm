#https://www.acmicpc.net/problem/14891
#톱니바퀴
#시뮬레이션 문제

import sys
input = sys.stdin.readline

def rotate(temp): #톱니바퀴 회전
    n = temp[0] #톱니번호
    d = temp[1] #회전방향(1=시계, -1=반시계)

    if d == 1: #시계방향
        end = graph[n][-1]
        for i in range(7, 0, -1):
            graph[n][i] = graph[n][i-1]
        graph[n][0] = end
    else: #반시계방향
        start = graph[n][0]
        for i in range(0, 7):
            graph[n][i] = graph[n][i+1]
        graph[n][7] = start

def check(temp): #톱니의 상황에 따라 회전
    can = [True for _ in range(4)] #톱니바퀴의 회전가능여부
    direction = [0 for _ in range(4)]
    n = temp[0] - 1 #회전할 톱니번호
    d = temp[1] #회전방향(1=시계, -1=반시계)
    direction[n] = d #처음 회전할 톱니

    nd = d
    for i in range(n, 3): #오른쪽 기준
        if can[i] == False: break
        if graph[i][2] != graph[i+1][6]: #맞물리는 톱니바퀴가 다를 떄
            direction[i+1] = -nd
            nd = -nd
        else: #같을 떄
            can[i+1] = False

    nd = d
    for i in range(n, 0, -1): #왼쪽 기준
        if can[i] == False: break
        if graph[i][6] != graph[i-1][2]: #맞물리는 톱니바퀴가 다를 때
            direction[i-1] = -nd
            nd = -nd
        else: #같을 떄
            can[i-1] = False

    #한번에 회전
    for i in range(4):
        if can[i] == True and direction[i] != 0: #회전 가능한 톱니번호일 때
            rotate([i, direction[i]])

graph= [] #톱니바퀴 정보
for i in range(4):
    graph.append(list(input().strip()))

k = int(input()) #회전 횟수

for i in range(k):
    order = list(map(int, input().split())) #톱니바퀴번호, 회전방향
    check(order)

sum = 0
for i in range(4):
    if graph[i][0] == "1": #S극인경우 점수
        sum += 2**i

print(sum)
