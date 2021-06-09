#https://www.acmicpc.net/problem/14888
#연산자 끼워넣기

def solution(n, arr, cal):
    max_s = -1e9; min_s = 1e9
    add = cal[0]; sub = cal[1]; mul = cal[2]; div = cal[3]

    def dfs(idx, value, add, sub, mul, div):
        nonlocal max_s, min_s
        if idx == n:
            max_s = max(max_s, value)
            min_s = min(min_s, value)
            return
        else:
            if add:
                dfs(idx + 1, value + arr[idx], add-1, sub, mul, div)
            if sub:
                dfs(idx + 1, value - arr[idx], add, sub-1, mul, div)
            if mul:
                dfs(idx + 1, value * arr[idx], add, sub, mul-1, div)
            if div:
                dfs(idx + 1, int(value/arr[idx]), add, sub, mul, div-1)

    dfs(1, arr[0], add, sub, mul, div)
    print(max_s)
    print(min_s)

n = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))

solution(n, arr, cal)
