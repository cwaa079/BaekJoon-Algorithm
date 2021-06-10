#https://www.acmicpc.net/problem/15658
#연산자 끼워넣기2
#백트래킹

def solution(n, arr, cal):
    add, sub, mul, div = cal[0], cal[1], cal[2], cal[3]
    max_s = -1e9; min_s = 1e9

    def dfs(idx, total, add, sub, mul, div):
        nonlocal max_s, min_s

        if idx == len(arr)-1:
            max_s = max(max_s, total)
            min_s = min(min_s, total)
            return

        if add:
            dfs(idx+1, total + arr[idx+1], add-1, sub, mul, div)
        if sub:
            dfs(idx+1, total - arr[idx+1], add, sub-1, mul, div)
        if mul:
            dfs(idx+1, total * arr[idx+1], add, sub, mul-1, div)
        if div:
            dfs(idx+1, int(total/arr[idx+1]), add, sub, mul, div-1)

    dfs(0, arr[0], add, sub, mul, div)
    print(max_s)
    print(min_s)

n = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))

solution(n, arr, cal)
