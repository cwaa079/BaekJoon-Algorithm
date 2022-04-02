#https://www.acmicpc.net/problem/2251
#물통

from collections import deque

def solution(limit):
    visited = [[[False] * 205 for _ in range(205)] for _ in range(205)]
    answer = [0] * 205

    def bfs():
        def move(cur, f, t):  # 물을 옮기는 방법 정의
            #t : 채우려는물통 / f : 비우려는물통
            res = [cur[0], cur[1], cur[2]]  # a,b,c
            if cur[f] + cur[t] <= limit[t]:
                res[t] = res[f] + res[t]  # 기존의 양 + 비운물통의 양으로 채워짐
                res[f] = 0  # 비우려는 물통이 완전히 비워짐
            else:
                res[f] -= limit[t] - res[t]  # 비울 물통인데 완전히 비워지지 않음.
                res[t] = limit[t]  # 채워지는 물통
            return res

        q = deque([[0, 0, limit[2]]]) #초기상태
        visited[0][0][limit[2]] = True

        while q:
            cur = q.popleft()
            if cur[0] == 0: #a물통에 아무것도 없으면
                answer[cur[2]] = True #c물통의 값 True
            for f in range(3):  # 비우는 물통
                for t in range(3):  # 채우려는 물통
                    if f == t: continue  # 왜냐면 같은 물통으로 옯길 수 없으니까
                    nxt = move(cur, f, t)  # 물을 옮기는 방법
                    if visited[nxt[0]][nxt[1]][nxt[2]] is False:
                        visited[nxt[0]][nxt[1]][nxt[2]] = True
                        q.append(nxt)

    bfs()
    for i in range(205):
        if answer[i]:
            print(i, end=' ')

    return 0


limit = list(map(int, input().split()))

solution(limit)
