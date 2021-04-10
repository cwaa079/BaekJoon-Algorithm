#https://www.acmicpc.net/problem/16235
#나무제태크
#큐활용한 시뮬레이션 문제

from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) #맵크기, 나무의 개수, 몇년후
now_a = [[5]*n for _ in range(n)] #현재 땅에 있는 양분
a = [] #추가되는 양분의 양
for i in range(n):
    a.append(list(map(int, input().split())))

tree = [[deque() for i in range(n)] for _ in range(n)] #심은 나무의 정보(x, y, 나무의 나이)
for i in range(m):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age) #나무의 나이

def spring_summer():
    for i in range(n):
        for j in range(n):
            len_tree = len(tree[i][j]) #한 땅에 있는 나무의 개수
            for k in range(len_tree):
                if tree[i][j][k] <= now_a[i][j]:#나무의 나이보다 양분이 같거나 많으면
                    now_a[i][j] -= tree[i][j][k] #양분 먹고
                    tree[i][j][k] += 1 #나이추가
                else: #작으면 죽고 양분이 됨
                    for _ in range(k, len_tree):
                        now_a[i][j] += tree[i][j].pop() // 2
                    break

def fall_winter():
    for i in range(n):
        for j in range(n):
            len_tree = len(tree[i][j]) #한 땅에 있는 나무의 개수
            for k in range(len_tree):
                if tree[i][j][k] % 5 == 0:
                    for r in range(8): #인접한 땅에 한개씩 나무 추가
                        x = i + dx[r]
                        y = j + dy[r]
                        if 0 <= x < n and 0 <= y < n:
                            tree[x][y].appendleft(1) #나이가 어린순으로 정렬
            now_a[i][j] += a[i][j]


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(k):
    spring_summer()
    fall_winter()

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(tree[i][j])

print(cnt)
