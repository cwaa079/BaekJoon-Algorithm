#https://www.acmicpc.net/problem/15665
#N과 M(11)

'''
같은 수 여러번 가능 -> 방문처리X
중복된 수열은 안됨 -> used함수를 통해 일일히 확인
'''
def solution(n, m, arr):
    arr.sort()
    ans = []

    def dfs():
        if len(ans) == m:
            print(' '.join(map(str, ans)), end = ' ')
            print()
            return

        used = [False for _ in range(max(arr)+1)]

        for i in range(n):
            if not used[arr[i]]:
                ans.append(arr[i])
                used[arr[i]] = True
                dfs()
                ans.pop()

    return dfs()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
