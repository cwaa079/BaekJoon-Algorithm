#https://www.acmicpc.net/problem/14500
#테트로미노
#memory:125236
#time:456ms

import sys
n, m = map(int, sys.stdin.readline().split()) #종이의 세로, 가로크기
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #종이의 수 입력

tetromino = [ [(0,0), (0,1), (1,0), (1,1)], # ㅁ
              [(0,0), (0,1), (0,2), (0,3)], # ㅡ
              [(0,0), (1,0), (2,0), (3,0)], # ㅣ
              [(0,0), (0,1), (0,2), (1,0)],
              [(1,0), (1,1), (1,2), (0,2)],
              [(0,0), (1,0), (1,1), (1,2)], # ㄴ
              [(0,0), (0,1), (0,2), (1,2)], # ㄱ
              [(0,0), (1,0), (2,0), (2,1)],
              [(2,0), (2,1), (1,1), (0,1)],
              [(0,0), (0,1), (1,0), (2,0)],
              [(0,0), (0,1), (1,1), (2,1)],
              [(0,0), (0,1), (0,2), (1,1)], # ㅜ
              [(1,0), (1,1), (1,2), (0,1)], # ㅗ
              [(0,0), (1,0), (2,0), (1,1)], # ㅏ
              [(1,0), (0,1), (1,1), (2,1)], # ㅓ
              [(1,0), (2,0), (0,1), (1,1)],
              [(0,0), (1,0), (1,1), (2,1)],
              [(1,0), (0,1), (1,1), (0,2)],
              [(0,0), (0,1), (1,1), (1,2)]
            ]

def find(x,y): #모양에 따른 최대값 찾기
    global max_value
    for i in range(19):
        temp = 0
        for j in range(4):
            try:
                nx = x + tetromino[i][j][0]
                ny = y + tetromino[i][j][1]
                temp += paper[nx][ny]
            except IndexError:
                continue
        max_value = max(max_value, temp)  # 현재 모양의 최대값

def solve():
    for i in range(n):
        for j in range(m):
            find(i, j)

max_value = -1 #최대값
solve()
print(max_value)
