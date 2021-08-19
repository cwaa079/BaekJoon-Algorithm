#https://www.acmicpc.net/problem/15664
#N과 M(10)

"""
중복된 수열을 체크하는데 문자열로 만들어서 딕셔너리 활용 : 4ms 더 빨라짐. (84ms -> 80ms)
"""

def solution(n, m, arr):
    arr.sort()
    check = {}
    ans = []
    visited = [False for _ in range(n)]

    def dfs(depth):
        if depth == m:
            s = ' '.join(map(str, ans))
            if s not in check:
                check[s] = 1
                print(s)
            return

        for i in range(n):
            if visited[i] is False:
                if depth == 0 or ans[-1] <= arr[i]:
                    ans.append(arr[i])
                    visited[i] = True
                    dfs(depth+1)
                    ans.pop()
                    visited[i] = False

    return dfs(0)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
