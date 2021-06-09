#https://www.acmicpc.net/problem/1759
#암호 만들기
#백트래킹으로 풀되 dfs사용

def solution(l, c, arr):
    arr.sort()
    temp = []
    visited = [False for _ in range(c)]
    def dfs(idx):
        if len(temp) == l:
            vo, co = 0, 0
            for i in range(l):
                if temp[i] in 'aeiou': vo += 1
                else: co += 1

            if vo>=1 and co>=2:
                print(''.join(temp))
            return

        for i in range(idx, c): #사전순으로 정렬하기 위해
            if visited[i] is False:
                temp.append(arr[i])
                visited[i] = True
                dfs(i+1)
                visited[i] = False
                temp.pop()
    dfs(0)

l, c = map(int, input().split())
arr = list(map(str, input().split()))

solution(l, c, arr)
