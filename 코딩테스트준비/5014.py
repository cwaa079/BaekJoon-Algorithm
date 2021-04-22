#https://www.acmicpc.net/problem/5014
#스타트링크
#BFS

f, s, g, u, d = map(int, input().split())
cnt = [-1] * (f+1)

def bfs(g, s):
    cnt[s] = 0
    q = deque([s])
    while q:
        now = q.popleft()

        if now == g:
            return cnt[now]

        for nstep in (now + u, now - d):
            if 0 < nstep <= f and cnt[nstep] == -1:
                q.append(nstep)
                cnt[nstep] = cnt[now] + 1
    return "use the stairs"

print(bfs(g,s))
