#https://www.acmicpc.net/problem/15656
#N과 M(7)

def solution(n, m, arr):
    arr.sort()
    num = []
    def dfs():
        if len(num) == m:
            print(' '.join(map(str, num)), end=" ")
            print()
            return

        for i in range(n):
            num.append(arr[i])
            dfs()
            num.pop()

    return dfs()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
