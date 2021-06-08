#https://www.acmicpc.net/problem/10819

from itertools import permutations

def solution(n, arr):
    temp = list(permutations(arr, n))
    max_s = -1e9
    for now in temp:
        total = 0
        for i in range(n-1):
            now = list(now)
            total += abs(now[i] - now[i+1])
        max_s = max(max_s, total)

    return max_s

n = int(input())
arr = list(map(int, input().split()))
print(solution(n, arr))
