#https://www.acmicpc.net/problem/1182
#부분수열 합 구하기
#재귀함수(dfs) 사용 (이론 상 백트래킹과 같음)

def solution(n, s, arr):
    cnt = 0
    def dfs(idx, total):
        nonlocal cnt
        if idx == n: return

        total += arr[idx]
        if total == s:
            cnt += 1

        dfs(idx+1, total)
        dfs(idx+1, total - arr[idx])

    dfs(0, 0)
    return cnt

n, s = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(n, s, arr))
