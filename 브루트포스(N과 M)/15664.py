#https://www.acmicpc.net/problem/15664
#N과 M(10)

'''
한번에 하나의 수 -> 방문처리중
중복된 수열X -> used함수를 통해 일일히 확인
비내림차순 -> depth로 이전 수와 현재 수 비교
'''

def solution(n, m, arr):
    visited = [False for _ in range(n)]
    arr.sort()
    num = []

    def dfs(depth):
        if depth == m:
            print(' '.join(map(str, num)))
            return
        used = [False for _ in range(max(arr)+1)]
        for i in range(n):
            if depth == 0 or num[depth-1] <= arr[i]:
                if not visited[i] and not used[arr[i]]:
                    num.append(arr[i]) #삽입
                    visited[i] = True #방문체크
                    used[arr[i]] = True #해당숫자완료(중복확인)
                    dfs(depth+1)
                    visited[i] = False
                    num.pop()
    return dfs(0)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
