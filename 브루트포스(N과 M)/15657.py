#https://www.acmicpc.net/problem/15657
#N과 M(8)

def solution(n, m, arr):
    arr.sort()
    num = []

    def dfs(depth):
        if depth == m:
            print(' '.join(map(str, num)), end=' ')
            print()
            return

        for i in range(n):
            if depth == 0 or num[depth - 1] <= arr[i]:
                num.append(arr[i])
                dfs(depth + 1)
                num.pop()

    return dfs(0)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
