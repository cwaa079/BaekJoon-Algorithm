#https://www.acmicpc.net/problem/15663
#N과 

def solution(n, m, arr):
    visited = [False for _ in range(n)]
    arr.sort()
    num = []

    def dfs():
        if len(num) == m:
            print(' '.join(map(str, num)))
            return
        used = [False for _ in range(max(arr)+1)]
        for i in range(n):
            if not visited[i] and not used[arr[i]]:
                num.append(arr[i]) #삽입
                visited[i] = True #방문체크
                used[arr[i]] = True #해당숫자완료(중복확인)
                dfs()
                visited[i] = False
                num.pop()
    return dfs()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
