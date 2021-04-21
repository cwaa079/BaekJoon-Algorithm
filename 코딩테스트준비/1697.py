#https://www.acmicpc.net/problem/1697
#숨바꼭질
#BFS

from collections import deque
n, k = map(int, input().split()) #수빈, 동생위치
MAX = 100001

time = [0] * MAX

q = deque([n])
while q:
    now = q.popleft()
    if now == k:
        print(time[k])
        break

    for nstep in (now-1, now+1, now*2):
        if 0<=nstep<MAX and time[nstep] == 0:
            time[nstep] = time[now] + 1
            q.append(nstep)
