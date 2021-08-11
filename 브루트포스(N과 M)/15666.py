#https://www.acmicpc.net/problem/15666
#N과 M(12)

'''
딕셔너리 활용하면 더 간단하게 코드를 짤 수 있음.
'''

def solution(n, m, arr):
    arr.sort()
    ans = []
    d = {} #딕셔너리 자료형

    def dfs(depth):
        if depth == m:
            s = ' '.join(map(str, ans))
            if s not in d:
                d[s] = 1
                print(s)
            return

        for i in range(n):
            if depth == 0 or ans[-1] <= arr[i]:
                ans.append(arr[i])
                dfs(depth+1)
                ans.pop()

    return dfs(0)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
